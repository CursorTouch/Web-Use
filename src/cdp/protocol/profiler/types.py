"""CDP Profiler Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.runtime.types import CallFrame
    from cdp.protocol.runtime.types import ScriptId

class ProfileNode(TypedDict, total=True):
    """Profile node. Holds callsite information, execution statistics and child nodes."""
    id: int
    """Unique id of the node."""
    callFrame: CallFrame
    """Function location."""
    hitCount: NotRequired[int]
    """Number of samples where this node was on top of the call stack."""
    children: NotRequired[List[int]]
    """Child node ids."""
    deoptReason: NotRequired[str]
    """The reason of being not optimized. The function may be deoptimized or marked as don't optimize."""
    positionTicks: NotRequired[List[PositionTickInfo]]
    """An array of source position ticks."""
class Profile(TypedDict, total=True):
    """Profile."""
    nodes: List[ProfileNode]
    """The list of profile nodes. First item is the root node."""
    startTime: float
    """Profiling start timestamp in microseconds."""
    endTime: float
    """Profiling end timestamp in microseconds."""
    samples: NotRequired[List[int]]
    """Ids of samples top nodes."""
    timeDeltas: NotRequired[List[int]]
    """Time intervals between adjacent samples in microseconds. The first delta is relative to the profile startTime."""
class PositionTickInfo(TypedDict, total=True):
    """Specifies a number of samples attributed to a certain source position."""
    line: int
    """Source line number (1-based)."""
    ticks: int
    """Number of samples attributed to the source line."""
class CoverageRange(TypedDict, total=True):
    """Coverage data for a source range."""
    startOffset: int
    """JavaScript script source offset for the range start."""
    endOffset: int
    """JavaScript script source offset for the range end."""
    count: int
    """Collected execution count of the source range."""
class FunctionCoverage(TypedDict, total=True):
    """Coverage data for a JavaScript function."""
    functionName: str
    """JavaScript function name."""
    ranges: List[CoverageRange]
    """Source ranges inside the function with coverage data."""
    isBlockCoverage: bool
    """Whether coverage data for this function has block granularity."""
class ScriptCoverage(TypedDict, total=True):
    """Coverage data for a JavaScript script."""
    scriptId: ScriptId
    """JavaScript script id."""
    url: str
    """JavaScript script name or url."""
    functions: List[FunctionCoverage]
    """Functions contained in the script that has coverage data."""