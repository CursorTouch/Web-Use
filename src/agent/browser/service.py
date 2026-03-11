from src.agent.browser.config import BrowserConfig, BROWSER_ARGS, SECURITY_ARGS
from typing import Any, Optional, Callable
from pathlib import Path
from src.cdp import Client
import subprocess
import shutil
import os
import tempfile
import asyncio
import httpx
import sys


class Browser:
    def __init__(self, config: BrowserConfig = None):
        self.config = config if config else BrowserConfig()
        self._process: subprocess.Popen = None
        self._client: Client = None

    # ------------------------------------------------------------------
    # Context manager
    # ------------------------------------------------------------------

    async def __aenter__(self):
        await self.init_browser()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close_browser()

    # ------------------------------------------------------------------
    # Browser launch / connect
    # ------------------------------------------------------------------

    async def init_browser(self):
        if self.config.wss_url:
            ws_url = self.config.wss_url if not self.config.wss_url.startswith('http') \
                else await self._fetch_ws_url(self.config.wss_url)
            self._client = Client(ws_url)
            await self._client.__aenter__()
            return

        await self._resolve_ws_url()

        port = self.config.cdp_port
        for attempt in range(10):
            try:
                ws_url = await self._fetch_ws_url(f'http://localhost:{port}')
                self._client = Client(ws_url)
                await self._client.__aenter__()
                return
            except Exception:
                await asyncio.sleep(1.0)
        raise RuntimeError(f'Could not establish WebSocket connection on port {port}')

    async def get_cdp_client(self) -> Client:
        if self._client is None:
            await self.init_browser()
        return self._client

    async def _resolve_ws_url(self):
        if self.config.wss_url:
            return
        port = self.config.cdp_port
        if await self._is_port_responsive(port):
            if await self._is_correct_browser(port):
                return  # correct browser already running, just connect
            # Wrong browser on the port — kill entire process tree and wait for port to free
            self._kill_on_port(port)
            for _ in range(10):
                await asyncio.sleep(0.5)
                if not await self._is_port_responsive(port):
                    break
        self._process = self._launch_process()
        await self._wait_for_browser(port=port, timeout=15.0)

    async def _is_port_responsive(self, port: int) -> bool:
        try:
            async with httpx.AsyncClient() as http:
                await http.get(f'http://localhost:{port}/json/version', timeout=1.0)
                return True
        except Exception:
            return False

    async def _is_correct_browser(self, port: int) -> bool:
        try:
            async with httpx.AsyncClient() as http:
                resp = await http.get(f'http://localhost:{port}/json/version', timeout=1.0)
                browser_str = resp.json().get('Browser', '').lower()
            if self.config.browser == 'chrome':
                return 'chrome' in browser_str and 'edg' not in browser_str
            elif self.config.browser == 'edge':
                return 'edg' in browser_str
            return False
        except Exception:
            return False

    def _kill_on_port(self, port: int):
        try:
            if sys.platform == 'win32':
                result = subprocess.run(
                    ['netstat', '-ano'],
                    capture_output=True, text=True
                )
                pids = set()
                for line in result.stdout.splitlines():
                    if f':{port}' in line and 'LISTENING' in line:
                        pid = line.strip().split()[-1]
                        if pid.isdigit():
                            pids.add(pid)
                for pid in pids:
                    # /T kills the entire process tree (all child processes too)
                    subprocess.run(['taskkill', '/F', '/T', '/PID', pid], capture_output=True)
            else:
                result = subprocess.run(
                    ['lsof', '-ti', f':{port}'],
                    capture_output=True, text=True
                )
                for pid in result.stdout.strip().splitlines():
                    subprocess.run(['kill', '-9', pid.strip()], capture_output=True)
        except Exception:
            pass

    def _copy_auth_files(self, src_profile_dir: str, dst_dir: str):
        """Copy auth-bearing files from src Chrome profile into dst_dir.

        Copies key files from src/Default/ into dst/Default/ and also copies
        Local State (DPAPI encryption key on Windows) from src/ into dst/.
        """
        src_default = Path(src_profile_dir) / 'Default'
        dst_default = Path(dst_dir) / 'Default'
        dst_default.mkdir(parents=True, exist_ok=True)

        auth_items = [
            'Cookies',
            'Local Storage',
            'Session Storage',
            'Network Persistent State',
            'Preferences',
        ]
        for item in auth_items:
            s = src_default / item
            d = dst_default / item
            try:
                if s.is_dir():
                    shutil.copytree(s, d, dirs_exist_ok=True)
                elif s.is_file():
                    shutil.copy2(s, d)
            except Exception:
                pass  # skip locked or missing files

        # Local State lives at the root of the profile dir (not inside Default/)
        # and holds the DPAPI key Chrome uses to decrypt the Cookies file on Windows.
        try:
            local_state = Path(src_profile_dir) / 'Local State'
            if local_state.exists():
                shutil.copy2(local_state, Path(dst_dir) / 'Local State')
        except Exception:
            pass

    def _resolve_user_data_dir(self) -> str:
        """Determine the user data directory to launch Chrome with.

        Three scenarios:
        1. use_system_profile=True
           → copy real Chrome profile auth files into a fresh temp dir each launch.
             Safe to use while Chrome is open; session data is discarded after.

        2. user_data_dir is a custom path (not the real Chrome profile)
           → persistent agent profile. On the very first run (Default/ absent),
             seed it with auth files from the real Chrome profile so the agent
             starts already logged in. Subsequent runs reuse what's already there.

        3. user_data_dir is None
           → completely fresh temp profile, no cookies, not logged into anything.
        """
        system_profile = self.config.get_system_profile_dir()

        if self.config.use_system_profile:
            # Always copy to a fresh temp dir — never touch the real profile
            tmp = tempfile.mkdtemp(prefix='web-use-profile-')
            if system_profile:
                self._copy_auth_files(system_profile, tmp)
            return tmp

        if self.config.user_data_dir:
            custom = Path(self.config.user_data_dir)
            is_real_profile = (
                system_profile and
                custom.resolve() == Path(system_profile).resolve()
            )
            if is_real_profile:
                # Treat the same as use_system_profile — avoid lock conflict
                tmp = tempfile.mkdtemp(prefix='web-use-profile-')
                self._copy_auth_files(str(custom), tmp)
                return tmp

            # Custom path: seed on first run only
            if not (custom / 'Default').exists() and system_profile:
                self._copy_auth_files(system_profile, str(custom))

            custom.mkdir(parents=True, exist_ok=True)
            return str(custom)

        # No path given — fresh throwaway profile
        return tempfile.mkdtemp(prefix='web-use-browser-')

    def _launch_process(self) -> subprocess.Popen:
        exe = self._get_executable()
        port = self.config.cdp_port
        user_data_dir = self._resolve_user_data_dir()

        args = [
            exe,
            f'--remote-debugging-port={port}',
            f'--user-data-dir={user_data_dir}',
            f'--download-default-directory={self.config.downloads_dir}',
        ] + BROWSER_ARGS + SECURITY_ARGS

        if self.config.headless:
            args.append('--headless=new')

        kwargs = {'stdout': subprocess.DEVNULL, 'stderr': subprocess.DEVNULL}
        if sys.platform == 'win32':
            kwargs['creationflags'] = subprocess.CREATE_NEW_PROCESS_GROUP

        return subprocess.Popen(args, **kwargs)

    def _get_executable(self) -> str:
        if self.config.browser_instance_dir:
            return self.config.browser_instance_dir

        browser = self.config.browser
        if sys.platform == 'win32':
            local = Path(os.environ.get('LOCALAPPDATA', ''))
            candidates = {
                'chrome': [
                    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
                    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                    str(local / 'Google' / 'Chrome' / 'Application' / 'chrome.exe'),
                ],
                'edge': [
                    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
                    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
                ],
            }
            for path in candidates.get(browser, []):
                if Path(path).exists():
                    return path
            raise FileNotFoundError(f'{browser.capitalize()} executable not found. Set browser_instance_dir in BrowserConfig.')
        elif sys.platform == 'darwin':
            paths = {
                'chrome': '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                'edge':   '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
            }
        else:
            paths = {
                'chrome': 'google-chrome',
                'edge':   'microsoft-edge',
            }
        return paths.get(browser, paths.get('chrome'))

    async def _wait_for_browser(self, port: int, timeout: float):
        deadline = asyncio.get_event_loop().time() + timeout
        while asyncio.get_event_loop().time() < deadline:
            try:
                async with httpx.AsyncClient() as http:
                    await http.get(f'http://localhost:{port}/json/version', timeout=2.0)
                    return
            except Exception:
                await asyncio.sleep(0.5)
        raise TimeoutError(f'Browser did not respond on port {port} within {timeout}s')

    async def _fetch_ws_url(self, http_url: str) -> str:
        async with httpx.AsyncClient() as http:
            resp = await http.get(f'{http_url.rstrip("/")}/json/version')
            return resp.json()['webSocketDebuggerUrl']

    async def close_browser(self):
        try:
            if self._client:
                await self._client.__aexit__(None, None, None)
        except Exception:
            pass
        finally:
            self._client = None

        try:
            if self._process:
                self._process.terminate()
                self._process.wait(timeout=5)
        except Exception:
            try:
                if self._process:
                    self._process.kill()
            except Exception:
                pass
        finally:
            self._process = None

    # ------------------------------------------------------------------
    # CDP wrappers
    # ------------------------------------------------------------------

    async def send(self, method: str, params: Optional[dict] = None, session_id: Optional[str] = None) -> Any:
        return await self._client.send(method, params or {}, session_id=session_id)

    def on(self, event: str, handler:Callable[[Any,Optional[str]], None]) -> None:
        self._client.on(event, handler)
