"""CDP HeapProfiler Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class HeapProfilerEvents:
    """
    Events for the HeapProfiler domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the HeapProfiler events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_add_heap_snapshot_chunk(self, callback: Callable[[addHeapSnapshotChunkEvent, str | None], None] | None = None) -> None:
        """
    No description available for addHeapSnapshotChunk.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: addHeapSnapshotChunkEvent, session_id: str | None).
        """
        self.client.on('HeapProfiler.addHeapSnapshotChunk', callback)
    def on_heap_stats_update(self, callback: Callable[[heapStatsUpdateEvent, str | None], None] | None = None) -> None:
        """
    If heap objects tracking has been started then backend may send update for one or more fragments    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: heapStatsUpdateEvent, session_id: str | None).
        """
        self.client.on('HeapProfiler.heapStatsUpdate', callback)
    def on_last_seen_object_id(self, callback: Callable[[lastSeenObjectIdEvent, str | None], None] | None = None) -> None:
        """
    If heap objects tracking has been started then backend regularly sends a current value for last seen object id and corresponding timestamp. If the were changes in the heap since last event then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: lastSeenObjectIdEvent, session_id: str | None).
        """
        self.client.on('HeapProfiler.lastSeenObjectId', callback)
    def on_report_heap_snapshot_progress(self, callback: Callable[[reportHeapSnapshotProgressEvent, str | None], None] | None = None) -> None:
        """
    No description available for reportHeapSnapshotProgress.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: reportHeapSnapshotProgressEvent, session_id: str | None).
        """
        self.client.on('HeapProfiler.reportHeapSnapshotProgress', callback)
    def on_reset_profiles(self, callback: Callable[[resetProfilesEvent, str | None], None] | None = None) -> None:
        """
    No description available for resetProfiles.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: resetProfilesEvent, session_id: str | None).
        """
        self.client.on('HeapProfiler.resetProfiles', callback)