"""CDP LayerTree Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import LayerTreeMethods
from .events.service import LayerTreeEvents

if TYPE_CHECKING:
    from ...service import Client

class LayerTree(LayerTreeMethods, LayerTreeEvents):
    """
    Access the LayerTree domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the LayerTree domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        LayerTreeMethods.__init__(self, client)
        LayerTreeEvents.__init__(self, client)