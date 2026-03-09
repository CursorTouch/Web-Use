"""CDP IndexedDB Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import IndexedDBMethods
from .events.service import IndexedDBEvents

if TYPE_CHECKING:
    from ...service import Client

class IndexedDB(IndexedDBMethods, IndexedDBEvents):
    """
    Access the IndexedDB domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the IndexedDB domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        IndexedDBMethods.__init__(self, client)
        IndexedDBEvents.__init__(self, client)