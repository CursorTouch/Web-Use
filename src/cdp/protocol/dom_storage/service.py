"""CDP DOMStorage Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import DOMStorageMethods
from .events.service import DOMStorageEvents

if TYPE_CHECKING:
    from ...service import Client

class DOMStorage(DOMStorageMethods, DOMStorageEvents):
    """
    Query and modify DOM storage.
    """
    def __init__(self, client: Client):
        """
        Initialize the DOMStorage domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        DOMStorageMethods.__init__(self, client)
        DOMStorageEvents.__init__(self, client)