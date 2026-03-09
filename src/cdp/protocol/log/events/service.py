"""CDP Log Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class LogEvents:
    """
    Events for the Log domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Log events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_entry_added(self, callback: Callable[[entryAddedEvent, str | None], None] | None = None) -> None:
        """
    Issued when new message was logged.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: entryAddedEvent, session_id: str | None).
        """
        self.client.on('Log.entryAdded', callback)