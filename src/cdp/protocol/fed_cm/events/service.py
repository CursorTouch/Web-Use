"""CDP FedCm Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class FedCmEvents:
    """
    Events for the FedCm domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the FedCm events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_dialog_shown(self, callback: Callable[[dialogShownEvent, str | None], None] | None = None) -> None:
        """
    No description available for dialogShown.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: dialogShownEvent, session_id: str | None).
        """
        self.client.on('FedCm.dialogShown', callback)
    def on_dialog_closed(self, callback: Callable[[dialogClosedEvent, str | None], None] | None = None) -> None:
        """
    Triggered when a dialog is closed, either by user action, JS abort, or a command below.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: dialogClosedEvent, session_id: str | None).
        """
        self.client.on('FedCm.dialogClosed', callback)