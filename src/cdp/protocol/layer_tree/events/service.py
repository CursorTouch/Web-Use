"""CDP LayerTree Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class LayerTreeEvents:
    """
    Events for the LayerTree domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the LayerTree events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_layer_painted(self, callback: Callable[[layerPaintedEvent, str | None], None] | None = None) -> None:
        """
    No description available for layerPainted.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: layerPaintedEvent, session_id: str | None).
        """
        self.client.on('LayerTree.layerPainted', callback)
    def on_layer_tree_did_change(self, callback: Callable[[layerTreeDidChangeEvent, str | None], None] | None = None) -> None:
        """
    No description available for layerTreeDidChange.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: layerTreeDidChangeEvent, session_id: str | None).
        """
        self.client.on('LayerTree.layerTreeDidChange', callback)