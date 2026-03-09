"""CDP HeapProfiler Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.runtime.types import CallFrame

HeapSnapshotObjectId = str
"""Heap snapshot object id."""
class SamplingHeapProfileNode(TypedDict, total=True):
    """Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes."""
    callFrame: CallFrame
    """Function location."""
    selfSize: float
    """Allocations size in bytes for the node excluding children."""
    id: int
    """Node id. Ids are unique across all profiles collected between startSampling and stopSampling."""
    children: List[SamplingHeapProfileNode]
    """Child nodes."""
class SamplingHeapProfileSample(TypedDict, total=True):
    """A single sample from a sampling profile."""
    size: float
    """Allocation size in bytes attributed to the sample."""
    nodeId: int
    """Id of the corresponding profile tree node."""
    ordinal: float
    """Time-ordered sample ordinal number. It is unique across all profiles retrieved between startSampling and stopSampling."""
class SamplingHeapProfile(TypedDict, total=True):
    """Sampling profile."""
    head: SamplingHeapProfileNode
    samples: List[SamplingHeapProfileSample]