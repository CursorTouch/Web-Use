"""CDP Tracing Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

class MemoryDumpConfig(TypedDict, total=True):
    """Configuration for memory dump. Used only when "memory-infra" category is enabled."""
    pass
class TraceConfig(TypedDict, total=False):
    recordMode: NotRequired[Literal["recordUntilFull", "recordContinuously", "recordAsMuchAsPossible", "echoToConsole"]]
    """Controls how the trace buffer stores data. The default is recordUntilFull."""
    traceBufferSizeInKb: NotRequired[float]
    """Size of the trace buffer in kilobytes. If not specified or zero is passed, a default value of 200 MB would be used."""
    enableSampling: NotRequired[bool]
    """Turns on JavaScript stack sampling."""
    enableSystrace: NotRequired[bool]
    """Turns on system tracing."""
    enableArgumentFilter: NotRequired[bool]
    """Turns on argument filter."""
    includedCategories: NotRequired[List[str]]
    """Included category filters."""
    excludedCategories: NotRequired[List[str]]
    """Excluded category filters."""
    syntheticDelays: NotRequired[List[str]]
    """Configuration to synthesize the delays in tracing."""
    memoryDumpConfig: NotRequired[MemoryDumpConfig]
    """Configuration for memory dump triggers. Used only when "memory-infra" category is enabled."""
StreamFormat = Literal['json','proto']
"""Data format of a trace. Can be either the legacy JSON format or the protocol buffer format. Note that the JSON format will be deprecated soon."""
StreamCompression = Literal['none','gzip']
"""Compression type to use for traces returned via streams."""
MemoryDumpLevelOfDetail = Literal['background','light','detailed']
"""Details exposed when memory request explicitly declared. Keep consistent with memory_dump_request_args.h and memory_instrumentation.mojom"""
TracingBackend = Literal['auto','chrome','system']
"""Backend type to use for tracing. `chrome` uses the Chrome-integrated tracing service and is supported on all platforms. `system` is only supported on Chrome OS and uses the Perfetto system tracing service. `auto` chooses `system` when the perfettoConfig provided to Tracing.start specifies at least one non-Chrome data source; otherwise uses `chrome`."""