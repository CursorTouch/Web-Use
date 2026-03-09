"""CDP Input Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class InputEvents:
    """
    Events for the Input domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Input events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_drag_intercepted(self, callback: Callable[[dragInterceptedEvent, str | None], None] | None = None) -> None:
        """
    Emitted only when `Input.setInterceptDrags` is enabled. Use this data with `Input.dispatchDragEvent` to restore normal drag and drop behavior.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: dragInterceptedEvent, session_id: str | None).
        """
        self.client.on('Input.dragIntercepted', callback)