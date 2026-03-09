"""CDP Runtime Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class RuntimeEvents:
    """
    Events for the Runtime domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Runtime events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_binding_called(self, callback: Callable[[bindingCalledEvent, str | None], None] | None = None) -> None:
        """
    Notification is issued every time when binding is called.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: bindingCalledEvent, session_id: str | None).
        """
        self.client.on('Runtime.bindingCalled', callback)
    def on_console_api_called(self, callback: Callable[[consoleAPICalledEvent, str | None], None] | None = None) -> None:
        """
    Issued when console API was called.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: consoleAPICalledEvent, session_id: str | None).
        """
        self.client.on('Runtime.consoleAPICalled', callback)
    def on_exception_revoked(self, callback: Callable[[exceptionRevokedEvent, str | None], None] | None = None) -> None:
        """
    Issued when unhandled exception was revoked.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: exceptionRevokedEvent, session_id: str | None).
        """
        self.client.on('Runtime.exceptionRevoked', callback)
    def on_exception_thrown(self, callback: Callable[[exceptionThrownEvent, str | None], None] | None = None) -> None:
        """
    Issued when exception was thrown and unhandled.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: exceptionThrownEvent, session_id: str | None).
        """
        self.client.on('Runtime.exceptionThrown', callback)
    def on_execution_context_created(self, callback: Callable[[executionContextCreatedEvent, str | None], None] | None = None) -> None:
        """
    Issued when new execution context is created.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: executionContextCreatedEvent, session_id: str | None).
        """
        self.client.on('Runtime.executionContextCreated', callback)
    def on_execution_context_destroyed(self, callback: Callable[[executionContextDestroyedEvent, str | None], None] | None = None) -> None:
        """
    Issued when execution context is destroyed.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: executionContextDestroyedEvent, session_id: str | None).
        """
        self.client.on('Runtime.executionContextDestroyed', callback)
    def on_execution_contexts_cleared(self, callback: Callable[[executionContextsClearedEvent, str | None], None] | None = None) -> None:
        """
    Issued when all executionContexts were cleared in browser    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: executionContextsClearedEvent, session_id: str | None).
        """
        self.client.on('Runtime.executionContextsCleared', callback)
    def on_inspect_requested(self, callback: Callable[[inspectRequestedEvent, str | None], None] | None = None) -> None:
        """
    Issued when object should be inspected (for example, as a result of inspect() command line API call).    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: inspectRequestedEvent, session_id: str | None).
        """
        self.client.on('Runtime.inspectRequested', callback)