"""CDP Emulation Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class EmulationEvents:
    """
    Events for the Emulation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Emulation events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_virtual_time_budget_expired(self, callback: Callable[[virtualTimeBudgetExpiredEvent, str | None], None] | None = None) -> None:
        """
    Notification sent after the virtual time budget for the current VirtualTimePolicy has run out.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: virtualTimeBudgetExpiredEvent, session_id: str | None).
        """
        self.client.on('Emulation.virtualTimeBudgetExpired', callback)
    def on_screen_orientation_lock_changed(self, callback: Callable[[screenOrientationLockChangedEvent, str | None], None] | None = None) -> None:
        """
    Fired when a page calls screen.orientation.lock() or screen.orientation.unlock() while device emulation is enabled. This allows the DevTools frontend to update the emulated device orientation accordingly.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: screenOrientationLockChangedEvent, session_id: str | None).
        """
        self.client.on('Emulation.screenOrientationLockChanged', callback)