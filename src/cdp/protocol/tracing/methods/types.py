"""CDP Tracing Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.tracing.types import MemoryDumpLevelOfDetail
    from cdp.protocol.tracing.types import StreamCompression
    from cdp.protocol.tracing.types import StreamFormat
    from cdp.protocol.tracing.types import TraceConfig
    from cdp.protocol.tracing.types import TracingBackend




class recordClockSyncMarkerParameters(TypedDict, total=True):
    syncId: str
    """The ID of this clock sync marker"""
class requestMemoryDumpParameters(TypedDict, total=False):
    deterministic: NotRequired[bool]
    """Enables more deterministic results by forcing garbage collection"""
    levelOfDetail: NotRequired[MemoryDumpLevelOfDetail]
    """Specifies level of details in memory dump. Defaults to "detailed"."""
class startParameters(TypedDict, total=False):
    categories: NotRequired[str]
    """Category/tag filter"""
    options: NotRequired[str]
    """Tracing options"""
    bufferUsageReportingInterval: NotRequired[float]
    """If set, the agent will issue bufferUsage events at this interval, specified in milliseconds"""
    transferMode: NotRequired[Literal["ReportEvents", "ReturnAsStream"]]
    """Whether to report trace events as series of dataCollected events or to save trace to a stream (defaults to ReportEvents)."""
    streamFormat: NotRequired[StreamFormat]
    """Trace data format to use. This only applies when using ReturnAsStream transfer mode (defaults to json)."""
    streamCompression: NotRequired[StreamCompression]
    """Compression format to use. This only applies when using ReturnAsStream transfer mode (defaults to none)"""
    traceConfig: NotRequired[TraceConfig]
    perfettoConfig: NotRequired[str]
    """Base64-encoded serialized perfetto.protos.TraceConfig protobuf message When specified, the parameters categories, options, traceConfig are ignored. (Encoded as a base64 string when passed over JSON)"""
    tracingBackend: NotRequired[TracingBackend]
    """Backend type (defaults to auto)"""

class getCategoriesReturns(TypedDict):
    categories: List[str]
    """A list of supported tracing categories."""
class getTrackEventDescriptorReturns(TypedDict):
    descriptor: str
    """Base64-encoded serialized perfetto.protos.TrackEventDescriptor protobuf message. (Encoded as a base64 string when passed over JSON)"""

class requestMemoryDumpReturns(TypedDict):
    dumpGuid: str
    """GUID of the resulting global memory dump."""
    success: bool
    """True iff the global memory dump succeeded."""