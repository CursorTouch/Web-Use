"""CDP Media Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import MediaMethods
from .events.service import MediaEvents

if TYPE_CHECKING:
    from ...service import Client

class Media(MediaMethods, MediaEvents):
    """
    This domain allows detailed inspection of media elements.
    """
    def __init__(self, client: Client):
        """
        Initialize the Media domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        MediaMethods.__init__(self, client)
        MediaEvents.__init__(self, client)