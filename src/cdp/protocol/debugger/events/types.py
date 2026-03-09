"""CDP Debugger Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.debugger.types import CallFrame
    from cdp.protocol.debugger.types import DebugSymbols
    from cdp.protocol.debugger.types import ResolvedBreakpoint
    from cdp.protocol.debugger.types import ScriptLanguage
    from cdp.protocol.runtime.types import ExecutionContextId
    from cdp.protocol.runtime.types import ScriptId
    from cdp.protocol.runtime.types import StackTrace
    from cdp.protocol.runtime.types import StackTraceId

class pausedEvent(TypedDict, total=True):
    callFrames: List[CallFrame]
    """Call stack the virtual machine stopped on."""
    reason: Literal["ambiguous", "assert", "CSPViolation", "debugCommand", "DOM", "EventListener", "exception", "instrumentation", "OOM", "other", "promiseRejection", "XHR", "step"]
    """Pause reason."""
    data: NotRequired[Dict[str, Any]]
    """Object containing break-specific auxiliary properties."""
    hitBreakpoints: NotRequired[List[str]]
    """Hit breakpoints IDs"""
    asyncStackTrace: NotRequired[StackTrace]
    """Async stack trace, if any."""
    asyncStackTraceId: NotRequired[StackTraceId]
    """Async stack trace, if any."""
    asyncCallStackTraceId: NotRequired[StackTraceId]
    """Never present, will be removed."""
class resumedEvent(TypedDict, total=True):
    pass
class scriptFailedToParseEvent(TypedDict, total=True):
    scriptId: ScriptId
    """Identifier of the script parsed."""
    url: str
    """URL or name of the script parsed (if any)."""
    startLine: int
    """Line offset of the script within the resource with given URL (for script tags)."""
    startColumn: int
    """Column offset of the script within the resource with given URL."""
    endLine: int
    """Last line of the script."""
    endColumn: int
    """Length of the last line of the script."""
    executionContextId: ExecutionContextId
    """Specifies script creation context."""
    hash: str
    """Content hash of the script, SHA-256."""
    buildId: str
    """For Wasm modules, the content of the build_id custom section. For JavaScript the debugId magic comment."""
    executionContextAuxData: NotRequired[Dict[str, Any]]
    """Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'|'isolated'|'worker', frameId: string}"""
    sourceMapURL: NotRequired[str]
    """URL of source map associated with script (if any)."""
    hasSourceURL: NotRequired[bool]
    """True, if this script has sourceURL."""
    isModule: NotRequired[bool]
    """True, if this script is ES6 module."""
    length: NotRequired[int]
    """This script length."""
    stackTrace: NotRequired[StackTrace]
    """JavaScript top stack frame of where the script parsed event was triggered if available."""
    codeOffset: NotRequired[int]
    """If the scriptLanguage is WebAssembly, the code section offset in the module."""
    scriptLanguage: NotRequired[ScriptLanguage]
    """The language of the script."""
    embedderName: NotRequired[str]
    """The name the embedder supplied for this script."""
class scriptParsedEvent(TypedDict, total=True):
    scriptId: ScriptId
    """Identifier of the script parsed."""
    url: str
    """URL or name of the script parsed (if any)."""
    startLine: int
    """Line offset of the script within the resource with given URL (for script tags)."""
    startColumn: int
    """Column offset of the script within the resource with given URL."""
    endLine: int
    """Last line of the script."""
    endColumn: int
    """Length of the last line of the script."""
    executionContextId: ExecutionContextId
    """Specifies script creation context."""
    hash: str
    """Content hash of the script, SHA-256."""
    buildId: str
    """For Wasm modules, the content of the build_id custom section. For JavaScript the debugId magic comment."""
    executionContextAuxData: NotRequired[Dict[str, Any]]
    """Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'|'isolated'|'worker', frameId: string}"""
    isLiveEdit: NotRequired[bool]
    """True, if this script is generated as a result of the live edit operation."""
    sourceMapURL: NotRequired[str]
    """URL of source map associated with script (if any)."""
    hasSourceURL: NotRequired[bool]
    """True, if this script has sourceURL."""
    isModule: NotRequired[bool]
    """True, if this script is ES6 module."""
    length: NotRequired[int]
    """This script length."""
    stackTrace: NotRequired[StackTrace]
    """JavaScript top stack frame of where the script parsed event was triggered if available."""
    codeOffset: NotRequired[int]
    """If the scriptLanguage is WebAssembly, the code section offset in the module."""
    scriptLanguage: NotRequired[ScriptLanguage]
    """The language of the script."""
    debugSymbols: NotRequired[List[DebugSymbols]]
    """If the scriptLanguage is WebAssembly, the source of debug symbols for the module."""
    embedderName: NotRequired[str]
    """The name the embedder supplied for this script."""
    resolvedBreakpoints: NotRequired[List[ResolvedBreakpoint]]
    """The list of set breakpoints in this script if calls to setBreakpointByUrl matches this script's URL or hash. Clients that use this list can ignore the breakpointResolved event. They are equivalent."""