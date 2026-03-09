"""CDP IO Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import IOMethods
from .events.service import IOEvents

if TYPE_CHECKING:
    from ...service import Client

class IO(IOMethods, IOEvents):
    """
    Input/Output operations for streams produced by DevTools.
    """
    def __init__(self, client: Client):
        """
        Initialize the IO domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        IOMethods.__init__(self, client)
        IOEvents.__init__(self, client)