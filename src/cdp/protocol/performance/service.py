"""CDP Performance Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import PerformanceMethods
from .events.service import PerformanceEvents

if TYPE_CHECKING:
    from ...service import Client

class Performance(PerformanceMethods, PerformanceEvents):
    """
    Access the Performance domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Performance domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        PerformanceMethods.__init__(self, client)
        PerformanceEvents.__init__(self, client)