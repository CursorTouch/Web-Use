"""CDP DOMStorage Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class DOMStorageEvents:
    """
    Events for the DOMStorage domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the DOMStorage events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_dom_storage_item_added(self, callback: Callable[[domStorageItemAddedEvent, str | None], None] | None = None) -> None:
        """
    No description available for domStorageItemAdded.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: domStorageItemAddedEvent, session_id: str | None).
        """
        self.client.on('DOMStorage.domStorageItemAdded', callback)
    def on_dom_storage_item_removed(self, callback: Callable[[domStorageItemRemovedEvent, str | None], None] | None = None) -> None:
        """
    No description available for domStorageItemRemoved.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: domStorageItemRemovedEvent, session_id: str | None).
        """
        self.client.on('DOMStorage.domStorageItemRemoved', callback)
    def on_dom_storage_item_updated(self, callback: Callable[[domStorageItemUpdatedEvent, str | None], None] | None = None) -> None:
        """
    No description available for domStorageItemUpdated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: domStorageItemUpdatedEvent, session_id: str | None).
        """
        self.client.on('DOMStorage.domStorageItemUpdated', callback)
    def on_dom_storage_items_cleared(self, callback: Callable[[domStorageItemsClearedEvent, str | None], None] | None = None) -> None:
        """
    No description available for domStorageItemsCleared.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: domStorageItemsClearedEvent, session_id: str | None).
        """
        self.client.on('DOMStorage.domStorageItemsCleared', callback)