"""CDP CacheStorage Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import CacheStorageMethods
from .events.service import CacheStorageEvents

if TYPE_CHECKING:
    from ...service import Client

class CacheStorage(CacheStorageMethods, CacheStorageEvents):
    """
    Access the CacheStorage domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the CacheStorage domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        CacheStorageMethods.__init__(self, client)
        CacheStorageEvents.__init__(self, client)