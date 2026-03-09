"""CDP HeapProfiler Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.heap_profiler.types import HeapSnapshotObjectId
    from cdp.protocol.heap_profiler.types import SamplingHeapProfile
    from cdp.protocol.runtime.types import RemoteObject
    from cdp.protocol.runtime.types import RemoteObjectId

class addInspectedHeapObjectParameters(TypedDict, total=True):
    heapObjectId: HeapSnapshotObjectId
    """Heap snapshot object id to be accessible by means of $x command line API."""



class getHeapObjectIdParameters(TypedDict, total=True):
    objectId: RemoteObjectId
    """Identifier of the object to get heap object id for."""
class getObjectByHeapObjectIdParameters(TypedDict, total=True):
    objectId: HeapSnapshotObjectId
    objectGroup: NotRequired[str]
    """Symbolic group name that can be used to release multiple objects."""

class startSamplingParameters(TypedDict, total=False):
    samplingInterval: NotRequired[float]
    """Average sample interval in bytes. Poisson distribution is used for the intervals. The default value is 32768 bytes."""
    stackDepth: NotRequired[float]
    """Maximum stack depth. The default value is 128."""
    includeObjectsCollectedByMajorGC: NotRequired[bool]
    """By default, the sampling heap profiler reports only objects which are still alive when the profile is returned via getSamplingProfile or stopSampling, which is useful for determining what functions contribute the most to steady-state memory usage. This flag instructs the sampling heap profiler to also include information about objects discarded by major GC, which will show which functions cause large temporary memory usage or long GC pauses."""
    includeObjectsCollectedByMinorGC: NotRequired[bool]
    """By default, the sampling heap profiler reports only objects which are still alive when the profile is returned via getSamplingProfile or stopSampling, which is useful for determining what functions contribute the most to steady-state memory usage. This flag instructs the sampling heap profiler to also include information about objects discarded by minor GC, which is useful when tuning a latency-sensitive application for minimal GC activity."""
class startTrackingHeapObjectsParameters(TypedDict, total=False):
    trackAllocations: NotRequired[bool]

class stopTrackingHeapObjectsParameters(TypedDict, total=False):
    reportProgress: NotRequired[bool]
    """If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken when the tracking is stopped."""
    treatGlobalObjectsAsRoots: NotRequired[bool]
    """Deprecated in favor of exposeInternals."""
    captureNumericValue: NotRequired[bool]
    """If true, numerical values are included in the snapshot"""
    exposeInternals: NotRequired[bool]
    """If true, exposes internals of the snapshot."""
class takeHeapSnapshotParameters(TypedDict, total=False):
    reportProgress: NotRequired[bool]
    """If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken."""
    treatGlobalObjectsAsRoots: NotRequired[bool]
    """If true, a raw snapshot without artificial roots will be generated. Deprecated in favor of exposeInternals."""
    captureNumericValue: NotRequired[bool]
    """If true, numerical values are included in the snapshot"""
    exposeInternals: NotRequired[bool]
    """If true, exposes internals of the snapshot."""




class getHeapObjectIdReturns(TypedDict):
    heapSnapshotObjectId: HeapSnapshotObjectId
    """Id of the heap snapshot object corresponding to the passed remote object id."""
class getObjectByHeapObjectIdReturns(TypedDict):
    result: RemoteObject
    """Evaluation result."""
class getSamplingProfileReturns(TypedDict):
    profile: SamplingHeapProfile
    """Return the sampling profile being collected."""


class stopSamplingReturns(TypedDict):
    profile: SamplingHeapProfile
    """Recorded sampling heap profile."""