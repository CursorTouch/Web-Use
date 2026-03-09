"""CDP Profiler Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import ProfilerMethods
from .events.service import ProfilerEvents

if TYPE_CHECKING:
    from ...service import Client

class Profiler(ProfilerMethods, ProfilerEvents):
    """
    Access the Profiler domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Profiler domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        ProfilerMethods.__init__(self, client)
        ProfilerEvents.__init__(self, client)