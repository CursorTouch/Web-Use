from __future__ import annotations
from src.agent.watchdog.base import BaseWatchdog


class CrashWatchdog(BaseWatchdog):
    """Detects tab crashes and cleans up session state.

    Chrome sends Inspector.targetCrashed in the context of the crashed
    page's session. Without this the agent hangs indefinitely waiting
    for a response from a dead renderer.
    """

    async def attach(self) -> None:
        self.session.browser.on('Inspector.targetCrashed', self._on_crash)

    def _on_crash(self, event, session_id=None) -> None:
        if not session_id:
            return

        # Find which target this session belongs to
        target_id = next(
            (tid for tid, sid in self.session._sessions.items() if sid == session_id),
            None,
        )
        print(f'[CrashWatchdog] Tab crashed (target={target_id}, session={session_id})')

        if target_id:
            self.session._targets.pop(target_id, None)
            self.session._sessions.pop(target_id, None)
            self.session._lifecycle.pop(session_id, None)

            # Signal any pending page-load waiter so it doesn't hang
            ready = self.session._page_ready.pop(session_id, None)
            if ready:
                ready.set()

            # Switch current target to another tab if possible
            if self.session._current_target_id == target_id:
                self.session._current_target_id = (
                    next(iter(self.session._sessions), None)
                )
