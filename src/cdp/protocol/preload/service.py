"""CDP Preload Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import PreloadMethods
from .events.service import PreloadEvents

if TYPE_CHECKING:
    from ...service import Client

class Preload(PreloadMethods, PreloadEvents):
    """
    Access the Preload domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Preload domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        PreloadMethods.__init__(self, client)
        PreloadEvents.__init__(self, client)