"""CDP DeviceAccess Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class DeviceAccessEvents:
    """
    Events for the DeviceAccess domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the DeviceAccess events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_device_request_prompted(self, callback: Callable[[deviceRequestPromptedEvent, str | None], None] | None = None) -> None:
        """
    A device request opened a user prompt to select a device. Respond with the selectPrompt or cancelPrompt command.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: deviceRequestPromptedEvent, session_id: str | None).
        """
        self.client.on('DeviceAccess.deviceRequestPrompted', callback)