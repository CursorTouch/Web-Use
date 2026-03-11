import platformdirs
import os
import platform
from dataclasses import dataclass
from typing import Literal
from pathlib import Path

def _get_browser_user_data_dir(browser: str) -> str:
    """Retrieve the standard user data directory for the specified browser."""
    system = platform.system()
    home = Path.home()
    
    if system == "Windows":
        local = Path(os.environ.get("LOCALAPPDATA", home / "AppData" / "Local"))
        if browser == 'chrome':
            return (local / "Google" / "Chrome" / "User Data").as_posix()
        elif browser == 'edge':
            return (local / "Microsoft" / "Edge" / "User Data").as_posix()
    elif system == "Darwin":
        support = home / "Library" / "Application Support"
        if browser == 'chrome':
            return (support / "Google" / "Chrome").as_posix()
        elif browser == 'edge':
            return (support / "Microsoft" / "Edge").as_posix()
    else:  # Linux/Unix
        config_home = Path(os.environ.get("XDG_CONFIG_HOME", home / ".config"))
        if browser == 'chrome':
            return (config_home / "google-chrome").as_posix()
        elif browser == 'edge':
            return (config_home / "microsoft-edge").as_posix()
    return None

@dataclass
class BrowserConfig:
    headless: bool = False
    wss_url: str = None          # Remote CDP endpoint (ws:// or http:// for /json/version)
    cdp_port: int = 9222         # Local remote-debugging port
    device: str = None
    browser_instance_dir: str = None  # Path to browser executable (optional override)
    downloads_dir: str = platformdirs.user_downloads_dir()
    browser: Literal['chrome', 'edge'] = 'edge'
    user_data_dir: str = None
    # use_system_profile=True: copy real Chrome profile to temp on every launch (safe when Chrome is open)
    # user_data_dir set to a custom path: seeds from real Chrome profile on first run, then persists
    # user_data_dir=None: fresh temporary profile with no auth
    use_system_profile: bool = False
    timeout: int = 60 * 1000
    slow_mo: int = 300

    def get_system_profile_dir(self) -> str | None:
        return _get_browser_user_data_dir(self.browser)

BROWSER_ARGS = [
    '--enable-blink-features=IdleDetection',
    '--disable-blink-features=AutomationControlled',
    '--disable-infobars',
    '--disable-background-timer-throttling',
    '--disable-popup-blocking',
    '--disable-backgrounding-occluded-windows',
    '--disable-renderer-backgrounding',
    '--disable-window-activation',
    '--disable-focus-on-load',
    '--no-first-run',
    '--no-default-browser-check',
    '--no-startup-window',
    '--window-position=0,0',
    '--force-device-scale-factor=1',
]

IGNORE_DEFAULT_ARGS = ['--enable-automation']
