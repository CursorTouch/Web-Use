"""CDP Storage Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import StorageMethods
from .events.service import StorageEvents

if TYPE_CHECKING:
    from ...service import Client

class Storage(StorageMethods, StorageEvents):
    """
    Access the Storage domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Storage domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        StorageMethods.__init__(self, client)
        StorageEvents.__init__(self, client)