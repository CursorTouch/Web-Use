from __future__ import annotations
from src.agent.watchdog.base import BaseWatchdog


class DialogWatchdog(BaseWatchdog):
    """Auto-dismisses JavaScript dialogs (alert/confirm/prompt).

    Without this, any alert() on a page blocks the entire renderer —
    no CDP commands go through until it is dismissed.
    """

    async def attach(self) -> None:
        self.session.browser.on('Page.javascriptDialogOpening', self._on_dialog)

    async def _on_dialog(self, event, session_id=None) -> None:
        if not session_id:
            return
        dialog_type = event.get('type', '')
        message     = event.get('message', '')
        print(f'[DialogWatchdog] Auto-dismissing {dialog_type}: "{message}"')
        try:
            await self.session.browser.send(
                'Page.handleJavaScriptDialog',
                {'accept': True, 'promptText': ''},
                session_id=session_id,
            )
        except Exception:
            pass
