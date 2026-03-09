"""CDP DOMDebugger Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class DOMDebuggerMethods:
    """
    Methods for the DOMDebugger domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the DOMDebugger methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def get_event_listeners(self, params: getEventListenersParameters | None = None, session_id: str | None = None) -> getEventListenersReturns:
        """
    Returns event listeners of the given object.    
        Args:
            params (getEventListenersParameters, optional): Parameters for the getEventListeners method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getEventListenersReturns: The result of the getEventListeners call.
        """
        return await self.client.send(method="DOMDebugger.getEventListeners", params=params, session_id=session_id)
    async def remove_dom_breakpoint(self, params: removeDOMBreakpointParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes DOM breakpoint that was set using `setDOMBreakpoint`.    
        Args:
            params (removeDOMBreakpointParameters, optional): Parameters for the removeDOMBreakpoint method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeDOMBreakpoint call.
        """
        return await self.client.send(method="DOMDebugger.removeDOMBreakpoint", params=params, session_id=session_id)
    async def remove_event_listener_breakpoint(self, params: removeEventListenerBreakpointParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes breakpoint on particular DOM event.    
        Args:
            params (removeEventListenerBreakpointParameters, optional): Parameters for the removeEventListenerBreakpoint method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeEventListenerBreakpoint call.
        """
        return await self.client.send(method="DOMDebugger.removeEventListenerBreakpoint", params=params, session_id=session_id)
    async def remove_xhr_breakpoint(self, params: removeXHRBreakpointParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes breakpoint from XMLHttpRequest.    
        Args:
            params (removeXHRBreakpointParameters, optional): Parameters for the removeXHRBreakpoint method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeXHRBreakpoint call.
        """
        return await self.client.send(method="DOMDebugger.removeXHRBreakpoint", params=params, session_id=session_id)
    async def set_break_on_csp_violation(self, params: setBreakOnCSPViolationParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets breakpoint on particular CSP violations.    
        Args:
            params (setBreakOnCSPViolationParameters, optional): Parameters for the setBreakOnCSPViolation method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setBreakOnCSPViolation call.
        """
        return await self.client.send(method="DOMDebugger.setBreakOnCSPViolation", params=params, session_id=session_id)
    async def set_dom_breakpoint(self, params: setDOMBreakpointParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets breakpoint on particular operation with DOM.    
        Args:
            params (setDOMBreakpointParameters, optional): Parameters for the setDOMBreakpoint method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDOMBreakpoint call.
        """
        return await self.client.send(method="DOMDebugger.setDOMBreakpoint", params=params, session_id=session_id)
    async def set_event_listener_breakpoint(self, params: setEventListenerBreakpointParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets breakpoint on particular DOM event.    
        Args:
            params (setEventListenerBreakpointParameters, optional): Parameters for the setEventListenerBreakpoint method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setEventListenerBreakpoint call.
        """
        return await self.client.send(method="DOMDebugger.setEventListenerBreakpoint", params=params, session_id=session_id)
    async def set_xhr_breakpoint(self, params: setXHRBreakpointParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets breakpoint on XMLHttpRequest.    
        Args:
            params (setXHRBreakpointParameters, optional): Parameters for the setXHRBreakpoint method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setXHRBreakpoint call.
        """
        return await self.client.send(method="DOMDebugger.setXHRBreakpoint", params=params, session_id=session_id)