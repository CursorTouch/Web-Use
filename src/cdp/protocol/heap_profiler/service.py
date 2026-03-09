"""CDP HeapProfiler Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import HeapProfilerMethods
from .events.service import HeapProfilerEvents

if TYPE_CHECKING:
    from ...service import Client

class HeapProfiler(HeapProfilerMethods, HeapProfilerEvents):
    """
    Access the HeapProfiler domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the HeapProfiler domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        HeapProfilerMethods.__init__(self, client)
        HeapProfilerEvents.__init__(self, client)