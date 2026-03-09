from src.agent.browser.config import BrowserConfig, BROWSER_ARGS, SECURITY_ARGS
from typing import Any, Optional, Callable
from pathlib import Path
from src.cdp import Client
import subprocess
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
        self._process = self._launch_process()
        await self._wait_for_browser(port=self.config.cdp_port, timeout=15.0)

    def _launch_process(self) -> subprocess.Popen:
        exe = self._get_executable()
        port = self.config.cdp_port
        user_data_dir = self.config.user_data_dir or tempfile.mkdtemp(prefix='web-use-browser-')

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
            paths = {
                'chrome': r'C:\Program Files\Google\Chrome\Application\chrome.exe',
                'edge':   r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
            }
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
