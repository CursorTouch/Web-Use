"""CDP Network Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import NetworkMethods
from .events.service import NetworkEvents

if TYPE_CHECKING:
    from ...service import Client

class Network(NetworkMethods, NetworkEvents):
    """
    Network domain allows tracking network activities of the page. It exposes information about http, file, data and other requests and responses, their headers, bodies, timing, etc.
    """
    def __init__(self, client: Client):
        """
        Initialize the Network domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        NetworkMethods.__init__(self, client)
        NetworkEvents.__init__(self, client)