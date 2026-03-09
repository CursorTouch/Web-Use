"""CDP Profiler Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class ProfilerEvents:
    """
    Events for the Profiler domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Profiler events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_console_profile_finished(self, callback: Callable[[consoleProfileFinishedEvent, str | None], None] | None = None) -> None:
        """
    No description available for consoleProfileFinished.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: consoleProfileFinishedEvent, session_id: str | None).
        """
        self.client.on('Profiler.consoleProfileFinished', callback)
    def on_console_profile_started(self, callback: Callable[[consoleProfileStartedEvent, str | None], None] | None = None) -> None:
        """
    Sent when new profile recording is started using console.profile() call.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: consoleProfileStartedEvent, session_id: str | None).
        """
        self.client.on('Profiler.consoleProfileStarted', callback)
    def on_precise_coverage_delta_update(self, callback: Callable[[preciseCoverageDeltaUpdateEvent, str | None], None] | None = None) -> None:
        """
    Reports coverage delta since the last poll (either from an event like this, or from `takePreciseCoverage` for the current isolate. May only be sent if precise code coverage has been started. This event can be trigged by the embedder to, for example, trigger collection of coverage data immediately at a certain point in time.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: preciseCoverageDeltaUpdateEvent, session_id: str | None).
        """
        self.client.on('Profiler.preciseCoverageDeltaUpdate', callback)