"""CDP Tracing Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.io.types import StreamHandle
    from cdp.protocol.tracing.types import StreamCompression
    from cdp.protocol.tracing.types import StreamFormat

class bufferUsageEvent(TypedDict, total=False):
    percentFull: NotRequired[float]
    """A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size."""
    eventCount: NotRequired[float]
    """An approximate number of events in the trace log."""
    value: NotRequired[float]
    """A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size."""
class dataCollectedEvent(TypedDict, total=True):
    value: List[Dict[str, Any]]
class tracingCompleteEvent(TypedDict, total=True):
    dataLossOccurred: bool
    """Indicates whether some trace data is known to have been lost, e.g. because the trace ring buffer wrapped around."""
    stream: NotRequired[StreamHandle]
    """A handle of the stream that holds resulting trace data."""
    traceFormat: NotRequired[StreamFormat]
    """Trace data format of returned stream."""
    streamCompression: NotRequired[StreamCompression]
    """Compression format of returned stream."""