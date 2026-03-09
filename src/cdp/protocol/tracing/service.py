"""CDP Tracing Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import TracingMethods
from .events.service import TracingEvents

if TYPE_CHECKING:
    from ...service import Client

class Tracing(TracingMethods, TracingEvents):
    """
    Access the Tracing domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Tracing domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        TracingMethods.__init__(self, client)
        TracingEvents.__init__(self, client)