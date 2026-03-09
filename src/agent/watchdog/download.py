from __future__ import annotations
from src.agent.watchdog.base import BaseWatchdog


class DownloadWatchdog(BaseWatchdog):
    """Tracks browser-native downloads via CDP Browser events.

    Covers downloads triggered by clicking buttons/links, not just
    explicit URL fetches. Also sets the download directory at the
    browser level so Chrome saves files to the configured path.
    """

    def __init__(self, session) -> None:
        super().__init__(session)
        self.downloads: dict[str, dict] = {}  # guid -> info

    async def attach(self) -> None:
        try:
            await self.session.browser.send('Browser.setDownloadBehavior', {
                'behavior':      'allow',
                'downloadPath':  self.session.browser.config.downloads_dir,
                'eventsEnabled': True,
            })
        except Exception:
            pass

        self.session.browser.on('Browser.downloadWillBegin', self._on_begin)
        self.session.browser.on('Browser.downloadProgress',  self._on_progress)

    def _on_begin(self, event, session_id=None) -> None:
        guid     = event.get('guid', '')
        filename = event.get('suggestedFilename', '')
        url      = event.get('url', '')
        self.downloads[guid] = {'url': url, 'filename': filename, 'state': 'started'}
        print(f'[DownloadWatchdog] Download started: {filename} ({url})')

    def _on_progress(self, event, session_id=None) -> None:
        guid  = event.get('guid', '')
        state = event.get('state', '')
        if guid not in self.downloads:
            return
        self.downloads[guid]['state'] = state
        filename = self.downloads[guid]['filename']
        if state == 'completed':
            print(f'[DownloadWatchdog] Download completed: {filename}')
        elif state == 'canceled':
            print(f'[DownloadWatchdog] Download canceled: {filename}')
