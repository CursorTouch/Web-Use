"""CDP Fetch Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import FetchMethods
from .events.service import FetchEvents

if TYPE_CHECKING:
    from ...service import Client

class Fetch(FetchMethods, FetchEvents):
    """
    A domain for letting clients substitute browser's network layer with client code.
    """
    def __init__(self, client: Client):
        """
        Initialize the Fetch domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        FetchMethods.__init__(self, client)
        FetchEvents.__init__(self, client)