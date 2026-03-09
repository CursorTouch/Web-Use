"""CDP Accessibility Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class AccessibilityEvents:
    """
    Events for the Accessibility domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Accessibility events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_load_complete(self, callback: Callable[[loadCompleteEvent, str | None], None] | None = None) -> None:
        """
    The loadComplete event mirrors the load complete event sent by the browser to assistive technology when the web page has finished loading.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: loadCompleteEvent, session_id: str | None).
        """
        self.client.on('Accessibility.loadComplete', callback)
    def on_nodes_updated(self, callback: Callable[[nodesUpdatedEvent, str | None], None] | None = None) -> None:
        """
    The nodesUpdated event is sent every time a previously requested node has changed the in tree.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: nodesUpdatedEvent, session_id: str | None).
        """
        self.client.on('Accessibility.nodesUpdated', callback)