"""CDP Debugger Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class DebuggerMethods:
    """
    Methods for the Debugger domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Debugger methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def continue_to_location(self, params: continueToLocationParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Continues execution until specific location is reached.    
        Args:
            params (continueToLocationParameters, optional): Parameters for the continueToLocation method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the continueToLocation call.
        """
        return await self.client.send(method="Debugger.continueToLocation", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables debugger for given page.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Debugger.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> enableReturns:
        """
    Enables debugger for the given page. Clients should not assume that the debugging has been enabled until the result for this command is received.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    enableReturns: The result of the enable call.
        """
        return await self.client.send(method="Debugger.enable", params=params, session_id=session_id)
    async def evaluate_on_call_frame(self, params: evaluateOnCallFrameParameters | None = None, session_id: str | None = None) -> evaluateOnCallFrameReturns:
        """
    Evaluates expression on a given call frame.    
        Args:
            params (evaluateOnCallFrameParameters, optional): Parameters for the evaluateOnCallFrame method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    evaluateOnCallFrameReturns: The result of the evaluateOnCallFrame call.
        """
        return await self.client.send(method="Debugger.evaluateOnCallFrame", params=params, session_id=session_id)
    async def get_possible_breakpoints(self, params: getPossibleBreakpointsParameters | None = None, session_id: str | None = None) -> getPossibleBreakpointsReturns:
        """
    Returns possible locations for breakpoint. scriptId in start and end range locations should be the same.    
        Args:
            params (getPossibleBreakpointsParameters, optional): Parameters for the getPossibleBreakpoints method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getPossibleBreakpointsReturns: The result of the getPossibleBreakpoints call.
        """
        return await self.client.send(method="Debugger.getPossibleBreakpoints", params=params, session_id=session_id)
    async def get_script_source(self, params: getScriptSourceParameters | None = None, session_id: str | None = None) -> getScriptSourceReturns:
        """
    Returns source for the script with given id.    
        Args:
            params (getScriptSourceParameters, optional): Parameters for the getScriptSource method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getScriptSourceReturns: The result of the getScriptSource call.
        """
        return await self.client.send(method="Debugger.getScriptSource", params=params, session_id=session_id)
    async def disassemble_wasm_module(self, params: disassembleWasmModuleParameters | None = None, session_id: str | None = None) -> disassembleWasmModuleReturns:
        """
    No description available for disassembleWasmModule.    
        Args:
            params (disassembleWasmModuleParameters, optional): Parameters for the disassembleWasmModule method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    disassembleWasmModuleReturns: The result of the disassembleWasmModule call.
        """
        return await self.client.send(method="Debugger.disassembleWasmModule", params=params, session_id=session_id)
    async def next_wasm_disassembly_chunk(self, params: nextWasmDisassemblyChunkParameters | None = None, session_id: str | None = None) -> nextWasmDisassemblyChunkReturns:
        """
    Disassemble the next chunk of lines for the module corresponding to the stream. If disassembly is complete, this API will invalidate the streamId and return an empty chunk. Any subsequent calls for the now invalid stream will return errors.    
        Args:
            params (nextWasmDisassemblyChunkParameters, optional): Parameters for the nextWasmDisassemblyChunk method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    nextWasmDisassemblyChunkReturns: The result of the nextWasmDisassemblyChunk call.
        """
        return await self.client.send(method="Debugger.nextWasmDisassemblyChunk", params=params, session_id=session_id)
    async def get_stack_trace(self, params: getStackTraceParameters | None = None, session_id: str | None = None) -> getStackTraceReturns:
        """
    Returns stack trace with given `stackTraceId`.    
        Args:
            params (getStackTraceParameters, optional): Parameters for the getStackTrace method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getStackTraceReturns: The result of the getStackTrace call.
        """
        return await self.client.send(method="Debugger.getStackTrace", params=params, session_id=session_id)
    async def pause(self, params: pauseParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Stops on the next JavaScript statement.    
        Args:
            params (pauseParameters, optional): Parameters for the pause method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the pause call.
        """
        return await self.client.send(method="Debugger.pause", params=params, session_id=session_id)
    async def remove_breakpoint(self, params: removeBreakpointParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes JavaScript breakpoint.    
        Args:
            params (removeBreakpointParameters, optional): Parameters for the removeBreakpoint method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeBreakpoint call.
        """
        return await self.client.send(method="Debugger.removeBreakpoint", params=params, session_id=session_id)
    async def restart_frame(self, params: restartFrameParameters | None = None, session_id: str | None = None) -> restartFrameReturns:
        """
    Restarts particular call frame from the beginning. The old, deprecated behavior of `restartFrame` is to stay paused and allow further CDP commands after a restart was scheduled. This can cause problems with restarting, so we now continue execution immediatly after it has been scheduled until we reach the beginning of the restarted frame.  To stay back-wards compatible, `restartFrame` now expects a `mode` parameter to be present. If the `mode` parameter is missing, `restartFrame` errors out.  The various return values are deprecated and `callFrames` is always empty. Use the call frames from the `Debugger#paused` events instead, that fires once V8 pauses at the beginning of the restarted function.    
        Args:
            params (restartFrameParameters, optional): Parameters for the restartFrame method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    restartFrameReturns: The result of the restartFrame call.
        """
        return await self.client.send(method="Debugger.restartFrame", params=params, session_id=session_id)
    async def resume(self, params: resumeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Resumes JavaScript execution.    
        Args:
            params (resumeParameters, optional): Parameters for the resume method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the resume call.
        """
        return await self.client.send(method="Debugger.resume", params=params, session_id=session_id)
    async def search_in_content(self, params: searchInContentParameters | None = None, session_id: str | None = None) -> searchInContentReturns:
        """
    Searches for given string in script content.    
        Args:
            params (searchInContentParameters, optional): Parameters for the searchInContent method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    searchInContentReturns: The result of the searchInContent call.
        """
        return await self.client.send(method="Debugger.searchInContent", params=params, session_id=session_id)
    async def set_async_call_stack_depth(self, params: setAsyncCallStackDepthParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables or disables async call stacks tracking.    
        Args:
            params (setAsyncCallStackDepthParameters, optional): Parameters for the setAsyncCallStackDepth method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAsyncCallStackDepth call.
        """
        return await self.client.send(method="Debugger.setAsyncCallStackDepth", params=params, session_id=session_id)
    async def set_blackbox_execution_contexts(self, params: setBlackboxExecutionContextsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Replace previous blackbox execution contexts with passed ones. Forces backend to skip stepping/pausing in scripts in these execution contexts. VM will try to leave blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.    
        Args:
            params (setBlackboxExecutionContextsParameters, optional): Parameters for the setBlackboxExecutionContexts method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setBlackboxExecutionContexts call.
        """
        return await self.client.send(method="Debugger.setBlackboxExecutionContexts", params=params, session_id=session_id)
    async def set_blackbox_patterns(self, params: setBlackboxPatternsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in scripts with url matching one of the patterns. VM will try to leave blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.    
        Args:
            params (setBlackboxPatternsParameters, optional): Parameters for the setBlackboxPatterns method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setBlackboxPatterns call.
        """
        return await self.client.send(method="Debugger.setBlackboxPatterns", params=params, session_id=session_id)
    async def set_blackboxed_ranges(self, params: setBlackboxedRangesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful. Positions array contains positions where blackbox state is changed. First interval isn't blackboxed. Array should be sorted.    
        Args:
            params (setBlackboxedRangesParameters, optional): Parameters for the setBlackboxedRanges method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setBlackboxedRanges call.
        """
        return await self.client.send(method="Debugger.setBlackboxedRanges", params=params, session_id=session_id)
    async def set_breakpoint(self, params: setBreakpointParameters | None = None, session_id: str | None = None) -> setBreakpointReturns:
        """
    Sets JavaScript breakpoint at a given location.    
        Args:
            params (setBreakpointParameters, optional): Parameters for the setBreakpoint method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setBreakpointReturns: The result of the setBreakpoint call.
        """
        return await self.client.send(method="Debugger.setBreakpoint", params=params, session_id=session_id)
    async def set_instrumentation_breakpoint(self, params: setInstrumentationBreakpointParameters | None = None, session_id: str | None = None) -> setInstrumentationBreakpointReturns:
        """
    Sets instrumentation breakpoint.    
        Args:
            params (setInstrumentationBreakpointParameters, optional): Parameters for the setInstrumentationBreakpoint method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setInstrumentationBreakpointReturns: The result of the setInstrumentationBreakpoint call.
        """
        return await self.client.send(method="Debugger.setInstrumentationBreakpoint", params=params, session_id=session_id)
    async def set_breakpoint_by_url(self, params: setBreakpointByUrlParameters | None = None, session_id: str | None = None) -> setBreakpointByUrlReturns:
        """
    Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this command is issued, all existing parsed scripts will have breakpoints resolved and returned in `locations` property. Further matching script parsing will result in subsequent `breakpointResolved` events issued. This logical breakpoint will survive page reloads.    
        Args:
            params (setBreakpointByUrlParameters, optional): Parameters for the setBreakpointByUrl method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setBreakpointByUrlReturns: The result of the setBreakpointByUrl call.
        """
        return await self.client.send(method="Debugger.setBreakpointByUrl", params=params, session_id=session_id)
    async def set_breakpoint_on_function_call(self, params: setBreakpointOnFunctionCallParameters | None = None, session_id: str | None = None) -> setBreakpointOnFunctionCallReturns:
        """
    Sets JavaScript breakpoint before each call to the given function. If another function was created from the same source as a given one, calling it will also trigger the breakpoint.    
        Args:
            params (setBreakpointOnFunctionCallParameters, optional): Parameters for the setBreakpointOnFunctionCall method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setBreakpointOnFunctionCallReturns: The result of the setBreakpointOnFunctionCall call.
        """
        return await self.client.send(method="Debugger.setBreakpointOnFunctionCall", params=params, session_id=session_id)
    async def set_breakpoints_active(self, params: setBreakpointsActiveParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Activates / deactivates all breakpoints on the page.    
        Args:
            params (setBreakpointsActiveParameters, optional): Parameters for the setBreakpointsActive method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setBreakpointsActive call.
        """
        return await self.client.send(method="Debugger.setBreakpointsActive", params=params, session_id=session_id)
    async def set_pause_on_exceptions(self, params: setPauseOnExceptionsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions, or caught exceptions, no exceptions. Initial pause on exceptions state is `none`.    
        Args:
            params (setPauseOnExceptionsParameters, optional): Parameters for the setPauseOnExceptions method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setPauseOnExceptions call.
        """
        return await self.client.send(method="Debugger.setPauseOnExceptions", params=params, session_id=session_id)
    async def set_return_value(self, params: setReturnValueParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Changes return value in top frame. Available only at return break position.    
        Args:
            params (setReturnValueParameters, optional): Parameters for the setReturnValue method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setReturnValue call.
        """
        return await self.client.send(method="Debugger.setReturnValue", params=params, session_id=session_id)
    async def set_script_source(self, params: setScriptSourceParameters | None = None, session_id: str | None = None) -> setScriptSourceReturns:
        """
    Edits JavaScript source live.  In general, functions that are currently on the stack can not be edited with a single exception: If the edited function is the top-most stack frame and that is the only activation of that function on the stack. In this case the live edit will be successful and a `Debugger.restartFrame` for the top-most function is automatically triggered.    
        Args:
            params (setScriptSourceParameters, optional): Parameters for the setScriptSource method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setScriptSourceReturns: The result of the setScriptSource call.
        """
        return await self.client.send(method="Debugger.setScriptSource", params=params, session_id=session_id)
    async def set_skip_all_pauses(self, params: setSkipAllPausesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc).    
        Args:
            params (setSkipAllPausesParameters, optional): Parameters for the setSkipAllPauses method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setSkipAllPauses call.
        """
        return await self.client.send(method="Debugger.setSkipAllPauses", params=params, session_id=session_id)
    async def set_variable_value(self, params: setVariableValueParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Changes value of variable in a callframe. Object-based scopes are not supported and must be mutated manually.    
        Args:
            params (setVariableValueParameters, optional): Parameters for the setVariableValue method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setVariableValue call.
        """
        return await self.client.send(method="Debugger.setVariableValue", params=params, session_id=session_id)
    async def step_into(self, params: stepIntoParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Steps into the function call.    
        Args:
            params (stepIntoParameters, optional): Parameters for the stepInto method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the stepInto call.
        """
        return await self.client.send(method="Debugger.stepInto", params=params, session_id=session_id)
    async def step_out(self, params: stepOutParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Steps out of the function call.    
        Args:
            params (stepOutParameters, optional): Parameters for the stepOut method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the stepOut call.
        """
        return await self.client.send(method="Debugger.stepOut", params=params, session_id=session_id)
    async def step_over(self, params: stepOverParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Steps over the statement.    
        Args:
            params (stepOverParameters, optional): Parameters for the stepOver method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the stepOver call.
        """
        return await self.client.send(method="Debugger.stepOver", params=params, session_id=session_id)