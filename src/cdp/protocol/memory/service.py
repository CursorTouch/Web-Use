"""CDP Memory Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import MemoryMethods
from .events.service import MemoryEvents

if TYPE_CHECKING:
    from ...service import Client

class Memory(MemoryMethods, MemoryEvents):
    """
    Access the Memory domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Memory domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        MemoryMethods.__init__(self, client)
        MemoryEvents.__init__(self, client)