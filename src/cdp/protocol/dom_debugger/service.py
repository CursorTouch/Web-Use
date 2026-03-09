"""CDP DOMDebugger Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import DOMDebuggerMethods
from .events.service import DOMDebuggerEvents

if TYPE_CHECKING:
    from ...service import Client

class DOMDebugger(DOMDebuggerMethods, DOMDebuggerEvents):
    """
    DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript execution will stop on these operations as if there was a regular breakpoint set.
    """
    def __init__(self, client: Client):
        """
        Initialize the DOMDebugger domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        DOMDebuggerMethods.__init__(self, client)
        DOMDebuggerEvents.__init__(self, client)