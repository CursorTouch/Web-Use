"""CDP EventBreakpoints Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class EventBreakpointsMethods:
    """
    Methods for the EventBreakpoints domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the EventBreakpoints methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def set_instrumentation_breakpoint(self, params: setInstrumentationBreakpointParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets breakpoint on particular native event.    
        Args:
            params (setInstrumentationBreakpointParameters, optional): Parameters for the setInstrumentationBreakpoint method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setInstrumentationBreakpoint call.
        """
        return await self.client.send(method="EventBreakpoints.setInstrumentationBreakpoint", params=params, session_id=session_id)
    async def remove_instrumentation_breakpoint(self, params: removeInstrumentationBreakpointParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes breakpoint on particular native event.    
        Args:
            params (removeInstrumentationBreakpointParameters, optional): Parameters for the removeInstrumentationBreakpoint method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeInstrumentationBreakpoint call.
        """
        return await self.client.send(method="EventBreakpoints.removeInstrumentationBreakpoint", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes all breakpoints    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="EventBreakpoints.disable", params=params, session_id=session_id)