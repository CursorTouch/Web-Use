"""CDP HeapProfiler Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

class addHeapSnapshotChunkEvent(TypedDict, total=True):
    chunk: str
class heapStatsUpdateEvent(TypedDict, total=True):
    statsUpdate: List[int]
    """An array of triplets. Each triplet describes a fragment. The first integer is the fragment index, the second integer is a total count of objects for the fragment, the third integer is a total size of the objects for the fragment."""
class lastSeenObjectIdEvent(TypedDict, total=True):
    lastSeenObjectId: int
    timestamp: float
class reportHeapSnapshotProgressEvent(TypedDict, total=True):
    done: int
    total: int
    finished: NotRequired[bool]
class resetProfilesEvent(TypedDict, total=True):
    pass