"""CDP Debugger Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import DebuggerMethods
from .events.service import DebuggerEvents

if TYPE_CHECKING:
    from ...service import Client

class Debugger(DebuggerMethods, DebuggerEvents):
    """
    Debugger domain exposes JavaScript debugging capabilities. It allows setting and removing breakpoints, stepping through execution, exploring stack traces, etc.
    """
    def __init__(self, client: Client):
        """
        Initialize the Debugger domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        DebuggerMethods.__init__(self, client)
        DebuggerEvents.__init__(self, client)