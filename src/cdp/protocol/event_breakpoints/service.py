"""CDP EventBreakpoints Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import EventBreakpointsMethods
from .events.service import EventBreakpointsEvents

if TYPE_CHECKING:
    from ...service import Client

class EventBreakpoints(EventBreakpointsMethods, EventBreakpointsEvents):
    """
    EventBreakpoints permits setting JavaScript breakpoints on operations and events occurring in native code invoked from JavaScript. Once breakpoint is hit, it is reported through Debugger domain, similarly to regular breakpoints being hit.
    """
    def __init__(self, client: Client):
        """
        Initialize the EventBreakpoints domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        EventBreakpointsMethods.__init__(self, client)
        EventBreakpointsEvents.__init__(self, client)