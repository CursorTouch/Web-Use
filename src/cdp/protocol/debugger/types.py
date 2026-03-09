"""CDP Debugger Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.runtime.types import RemoteObject
    from cdp.protocol.runtime.types import ScriptId

BreakpointId = str
"""Breakpoint identifier."""
CallFrameId = str
"""Call frame identifier."""
class Location(TypedDict, total=True):
    """Location in the source code."""
    scriptId: ScriptId
    """Script identifier as reported in the Debugger.scriptParsed."""
    lineNumber: int
    """Line number in the script (0-based)."""
    columnNumber: NotRequired[int]
    """Column number in the script (0-based)."""
class ScriptPosition(TypedDict, total=True):
    """Location in the source code."""
    lineNumber: int
    columnNumber: int
class LocationRange(TypedDict, total=True):
    """Location range within one script."""
    scriptId: ScriptId
    start: ScriptPosition
    end: ScriptPosition
class CallFrame(TypedDict, total=True):
    """JavaScript call frame. Array of call frames form the call stack."""
    callFrameId: CallFrameId
    """Call frame identifier. This identifier is only valid while the virtual machine is paused."""
    functionName: str
    """Name of the JavaScript function called on this call frame."""
    location: Location
    """Location in the source code."""
    scopeChain: List[Scope]
    """Scope chain for this call frame."""
    this: RemoteObject
    """this object for this call frame."""
    functionLocation: NotRequired[Location]
    """Location in the source code."""
    returnValue: NotRequired[RemoteObject]
    """The value being returned, if the function is at return point."""
    canBeRestarted: NotRequired[bool]
    """Valid only while the VM is paused and indicates whether this frame can be restarted or not. Note that a true value here does not guarantee that Debugger#restartFrame with this CallFrameId will be successful, but it is very likely."""
class Scope(TypedDict, total=True):
    """Scope description."""
    type: Literal["global", "local", "with", "closure", "catch", "block", "script", "eval", "module", "wasm-expression-stack"]
    """Scope type."""
    object: RemoteObject
    """Object representing the scope. For global and with scopes it represents the actual object; for the rest of the scopes, it is artificial transient object enumerating scope variables as its properties."""
    name: NotRequired[str]
    startLocation: NotRequired[Location]
    """Location in the source code where scope starts"""
    endLocation: NotRequired[Location]
    """Location in the source code where scope ends"""
class SearchMatch(TypedDict, total=True):
    """Search match for resource."""
    lineNumber: float
    """Line number in resource content."""
    lineContent: str
    """Line with match content."""
class BreakLocation(TypedDict, total=True):
    scriptId: ScriptId
    """Script identifier as reported in the Debugger.scriptParsed."""
    lineNumber: int
    """Line number in the script (0-based)."""
    columnNumber: NotRequired[int]
    """Column number in the script (0-based)."""
    type: NotRequired[Literal["debuggerStatement", "call", "return"]]
class WasmDisassemblyChunk(TypedDict, total=True):
    lines: List[str]
    """The next chunk of disassembled lines."""
    bytecodeOffsets: List[int]
    """The bytecode offsets describing the start of each line."""
ScriptLanguage = Literal['JavaScript','WebAssembly']
"""Enum of possible script languages."""
class DebugSymbols(TypedDict, total=True):
    """Debug symbols available for a wasm script."""
    type: Literal["SourceMap", "EmbeddedDWARF", "ExternalDWARF"]
    """Type of the debug symbols."""
    externalURL: NotRequired[str]
    """URL of the external symbol source."""
class ResolvedBreakpoint(TypedDict, total=True):
    breakpointId: BreakpointId
    """Breakpoint unique identifier."""
    location: Location
    """Actual breakpoint location."""