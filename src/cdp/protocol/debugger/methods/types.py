"""CDP Debugger Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.debugger.types import BreakLocation
    from cdp.protocol.debugger.types import BreakpointId
    from cdp.protocol.debugger.types import CallFrame
    from cdp.protocol.debugger.types import CallFrameId
    from cdp.protocol.debugger.types import Location
    from cdp.protocol.debugger.types import LocationRange
    from cdp.protocol.debugger.types import ScriptPosition
    from cdp.protocol.debugger.types import SearchMatch
    from cdp.protocol.debugger.types import WasmDisassemblyChunk
    from cdp.protocol.runtime.types import CallArgument
    from cdp.protocol.runtime.types import ExceptionDetails
    from cdp.protocol.runtime.types import RemoteObject
    from cdp.protocol.runtime.types import RemoteObjectId
    from cdp.protocol.runtime.types import ScriptId
    from cdp.protocol.runtime.types import StackTrace
    from cdp.protocol.runtime.types import StackTraceId
    from cdp.protocol.runtime.types import TimeDelta
    from cdp.protocol.runtime.types import UniqueDebuggerId

class continueToLocationParameters(TypedDict, total=True):
    location: Location
    """Location to continue to."""
    targetCallFrames: NotRequired[Literal["any", "current"]]

class enableParameters(TypedDict, total=False):
    maxScriptsCacheSize: NotRequired[float]
    """The maximum size in bytes of collected scripts (not referenced by other heap objects) the debugger can hold. Puts no limit if parameter is omitted."""
class evaluateOnCallFrameParameters(TypedDict, total=True):
    callFrameId: CallFrameId
    """Call frame identifier to evaluate on."""
    expression: str
    """Expression to evaluate."""
    objectGroup: NotRequired[str]
    """String object group name to put result into (allows rapid releasing resulting object handles using releaseObjectGroup)."""
    includeCommandLineAPI: NotRequired[bool]
    """Specifies whether command line API should be available to the evaluated expression, defaults to false."""
    silent: NotRequired[bool]
    """In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides setPauseOnException state."""
    returnByValue: NotRequired[bool]
    """Whether the result is expected to be a JSON object that should be sent by value."""
    generatePreview: NotRequired[bool]
    """Whether preview should be generated for the result."""
    throwOnSideEffect: NotRequired[bool]
    """Whether to throw an exception if side effect cannot be ruled out during evaluation."""
    timeout: NotRequired[TimeDelta]
    """Terminate execution after timing out (number of milliseconds)."""
class getPossibleBreakpointsParameters(TypedDict, total=True):
    start: Location
    """Start of range to search possible breakpoint locations in."""
    end: NotRequired[Location]
    """End of range to search possible breakpoint locations in (excluding). When not specified, end of scripts is used as end of range."""
    restrictToFunction: NotRequired[bool]
    """Only consider locations which are in the same (non-nested) function as start."""
class getScriptSourceParameters(TypedDict, total=True):
    scriptId: ScriptId
    """Id of the script to get source for."""
class disassembleWasmModuleParameters(TypedDict, total=True):
    scriptId: ScriptId
    """Id of the script to disassemble"""
class nextWasmDisassemblyChunkParameters(TypedDict, total=True):
    streamId: str
class getStackTraceParameters(TypedDict, total=True):
    stackTraceId: StackTraceId

class removeBreakpointParameters(TypedDict, total=True):
    breakpointId: BreakpointId
class restartFrameParameters(TypedDict, total=True):
    callFrameId: CallFrameId
    """Call frame identifier to evaluate on."""
    mode: NotRequired[Literal["StepInto"]]
    """The mode parameter must be present and set to 'StepInto', otherwise restartFrame will error out."""
class resumeParameters(TypedDict, total=False):
    terminateOnResume: NotRequired[bool]
    """Set to true to terminate execution upon resuming execution. In contrast to Runtime.terminateExecution, this will allows to execute further JavaScript (i.e. via evaluation) until execution of the paused code is actually resumed, at which point termination is triggered. If execution is currently not paused, this parameter has no effect."""
class searchInContentParameters(TypedDict, total=True):
    scriptId: ScriptId
    """Id of the script to search in."""
    query: str
    """String to search for."""
    caseSensitive: NotRequired[bool]
    """If true, search is case sensitive."""
    isRegex: NotRequired[bool]
    """If true, treats string parameter as regex."""
class setAsyncCallStackDepthParameters(TypedDict, total=True):
    maxDepth: int
    """Maximum depth of async call stacks. Setting to 0 will effectively disable collecting async call stacks (default)."""
class setBlackboxExecutionContextsParameters(TypedDict, total=True):
    uniqueIds: List[str]
    """Array of execution context unique ids for the debugger to ignore."""
class setBlackboxPatternsParameters(TypedDict, total=True):
    patterns: List[str]
    """Array of regexps that will be used to check script url for blackbox state."""
    skipAnonymous: NotRequired[bool]
    """If true, also ignore scripts with no source url."""
class setBlackboxedRangesParameters(TypedDict, total=True):
    scriptId: ScriptId
    """Id of the script."""
    positions: List[ScriptPosition]
class setBreakpointParameters(TypedDict, total=True):
    location: Location
    """Location to set breakpoint in."""
    condition: NotRequired[str]
    """Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true."""
class setInstrumentationBreakpointParameters(TypedDict, total=True):
    instrumentation: Literal["beforeScriptExecution", "beforeScriptWithSourceMapExecution"]
    """Instrumentation name."""
class setBreakpointByUrlParameters(TypedDict, total=True):
    lineNumber: int
    """Line number to set breakpoint at."""
    url: NotRequired[str]
    """URL of the resources to set breakpoint on."""
    urlRegex: NotRequired[str]
    """Regex pattern for the URLs of the resources to set breakpoints on. Either url or urlRegex must be specified."""
    scriptHash: NotRequired[str]
    """Script hash of the resources to set breakpoint on."""
    columnNumber: NotRequired[int]
    """Offset in the line to set breakpoint at."""
    condition: NotRequired[str]
    """Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true."""
class setBreakpointOnFunctionCallParameters(TypedDict, total=True):
    objectId: RemoteObjectId
    """Function object id."""
    condition: NotRequired[str]
    """Expression to use as a breakpoint condition. When specified, debugger will stop on the breakpoint if this expression evaluates to true."""
class setBreakpointsActiveParameters(TypedDict, total=True):
    active: bool
    """New value for breakpoints active state."""
class setPauseOnExceptionsParameters(TypedDict, total=True):
    state: Literal["none", "caught", "uncaught", "all"]
    """Pause on exceptions mode."""
class setReturnValueParameters(TypedDict, total=True):
    newValue: CallArgument
    """New return value."""
class setScriptSourceParameters(TypedDict, total=True):
    scriptId: ScriptId
    """Id of the script to edit."""
    scriptSource: str
    """New content of the script."""
    dryRun: NotRequired[bool]
    """If true the change will not actually be applied. Dry run may be used to get result description without actually modifying the code."""
    allowTopFrameEditing: NotRequired[bool]
    """If true, then scriptSource is allowed to change the function on top of the stack as long as the top-most stack frame is the only activation of that function."""
class setSkipAllPausesParameters(TypedDict, total=True):
    skip: bool
    """New value for skip pauses state."""
class setVariableValueParameters(TypedDict, total=True):
    scopeNumber: int
    """0-based number of scope as was listed in scope chain. Only 'local', 'closure' and 'catch' scope types are allowed. Other scopes could be manipulated manually."""
    variableName: str
    """Variable name."""
    newValue: CallArgument
    """New variable value."""
    callFrameId: CallFrameId
    """Id of callframe that holds variable."""
class stepIntoParameters(TypedDict, total=False):
    breakOnAsyncCall: NotRequired[bool]
    """Debugger will pause on the execution of the first async task which was scheduled before next pause."""
    skipList: NotRequired[List[LocationRange]]
    """The skipList specifies location ranges that should be skipped on step into."""

class stepOverParameters(TypedDict, total=False):
    skipList: NotRequired[List[LocationRange]]
    """The skipList specifies location ranges that should be skipped on step over."""


class enableReturns(TypedDict):
    debuggerId: UniqueDebuggerId
    """Unique identifier of the debugger."""
class evaluateOnCallFrameReturns(TypedDict):
    result: RemoteObject
    """Object wrapper for the evaluation result."""
    exceptionDetails: ExceptionDetails
    """Exception details."""
class getPossibleBreakpointsReturns(TypedDict):
    locations: List[BreakLocation]
    """List of the possible breakpoint locations."""
class getScriptSourceReturns(TypedDict):
    scriptSource: str
    """Script source (empty in case of Wasm bytecode)."""
    bytecode: str
    """Wasm bytecode. (Encoded as a base64 string when passed over JSON)"""
class disassembleWasmModuleReturns(TypedDict):
    streamId: str
    """For large modules, return a stream from which additional chunks of disassembly can be read successively."""
    totalNumberOfLines: int
    """The total number of lines in the disassembly text."""
    functionBodyOffsets: List[int]
    """The offsets of all function bodies, in the format [start1, end1, start2, end2, ...] where all ends are exclusive."""
    chunk: WasmDisassemblyChunk
    """The first chunk of disassembly."""
class nextWasmDisassemblyChunkReturns(TypedDict):
    chunk: WasmDisassemblyChunk
    """The next chunk of disassembly."""
class getStackTraceReturns(TypedDict):
    stackTrace: StackTrace


class restartFrameReturns(TypedDict):
    callFrames: List[CallFrame]
    """New stack trace."""
    asyncStackTrace: StackTrace
    """Async stack trace, if any."""
    asyncStackTraceId: StackTraceId
    """Async stack trace, if any."""

class searchInContentReturns(TypedDict):
    result: List[SearchMatch]
    """List of search matches."""




class setBreakpointReturns(TypedDict):
    breakpointId: BreakpointId
    """Id of the created breakpoint for further reference."""
    actualLocation: Location
    """Location this breakpoint resolved into."""
class setInstrumentationBreakpointReturns(TypedDict):
    breakpointId: BreakpointId
    """Id of the created breakpoint for further reference."""
class setBreakpointByUrlReturns(TypedDict):
    breakpointId: BreakpointId
    """Id of the created breakpoint for further reference."""
    locations: List[Location]
    """List of the locations this breakpoint resolved into upon addition."""
class setBreakpointOnFunctionCallReturns(TypedDict):
    breakpointId: BreakpointId
    """Id of the created breakpoint for further reference."""



class setScriptSourceReturns(TypedDict):
    callFrames: List[CallFrame]
    """New stack trace in case editing has happened while VM was stopped."""
    stackChanged: bool
    """Whether current call stack  was modified after applying the changes."""
    asyncStackTrace: StackTrace
    """Async stack trace, if any."""
    asyncStackTraceId: StackTraceId
    """Async stack trace, if any."""
    status: Literal["Ok", "CompileError", "BlockedByActiveGenerator", "BlockedByActiveFunction", "BlockedByTopLevelEsModuleChange"]
    """Whether the operation was successful or not. Only Ok denotes a successful live edit while the other enum variants denote why the live edit failed."""
    exceptionDetails: ExceptionDetails
    """Exception details if any. Only present when status is CompileError."""