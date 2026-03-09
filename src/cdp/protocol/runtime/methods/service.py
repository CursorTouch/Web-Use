"""CDP Runtime Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class RuntimeMethods:
    """
    Methods for the Runtime domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Runtime methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def await_promise(self, params: awaitPromiseParameters | None = None, session_id: str | None = None) -> awaitPromiseReturns:
        """
    Add handler to promise with given promise object id.    
        Args:
            params (awaitPromiseParameters, optional): Parameters for the awaitPromise method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    awaitPromiseReturns: The result of the awaitPromise call.
        """
        return await self.client.send(method="Runtime.awaitPromise", params=params, session_id=session_id)
    async def call_function_on(self, params: callFunctionOnParameters | None = None, session_id: str | None = None) -> callFunctionOnReturns:
        """
    Calls function with given declaration on the given object. Object group of the result is inherited from the target object.    
        Args:
            params (callFunctionOnParameters, optional): Parameters for the callFunctionOn method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    callFunctionOnReturns: The result of the callFunctionOn call.
        """
        return await self.client.send(method="Runtime.callFunctionOn", params=params, session_id=session_id)
    async def compile_script(self, params: compileScriptParameters | None = None, session_id: str | None = None) -> compileScriptReturns:
        """
    Compiles expression.    
        Args:
            params (compileScriptParameters, optional): Parameters for the compileScript method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    compileScriptReturns: The result of the compileScript call.
        """
        return await self.client.send(method="Runtime.compileScript", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables reporting of execution contexts creation.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Runtime.disable", params=params, session_id=session_id)
    async def discard_console_entries(self, params: discardConsoleEntriesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Discards collected exceptions and console API calls.    
        Args:
            params (discardConsoleEntriesParameters, optional): Parameters for the discardConsoleEntries method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the discardConsoleEntries call.
        """
        return await self.client.send(method="Runtime.discardConsoleEntries", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables reporting of execution contexts creation by means of `executionContextCreated` event. When the reporting gets enabled the event will be sent immediately for each existing execution context.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Runtime.enable", params=params, session_id=session_id)
    async def evaluate(self, params: evaluateParameters | None = None, session_id: str | None = None) -> evaluateReturns:
        """
    Evaluates expression on global object.    
        Args:
            params (evaluateParameters, optional): Parameters for the evaluate method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    evaluateReturns: The result of the evaluate call.
        """
        return await self.client.send(method="Runtime.evaluate", params=params, session_id=session_id)
    async def get_isolate_id(self, params: getIsolateIdParameters | None = None, session_id: str | None = None) -> getIsolateIdReturns:
        """
    Returns the isolate id.    
        Args:
            params (getIsolateIdParameters, optional): Parameters for the getIsolateId method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getIsolateIdReturns: The result of the getIsolateId call.
        """
        return await self.client.send(method="Runtime.getIsolateId", params=params, session_id=session_id)
    async def get_heap_usage(self, params: getHeapUsageParameters | None = None, session_id: str | None = None) -> getHeapUsageReturns:
        """
    Returns the JavaScript heap usage. It is the total usage of the corresponding isolate not scoped to a particular Runtime.    
        Args:
            params (getHeapUsageParameters, optional): Parameters for the getHeapUsage method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getHeapUsageReturns: The result of the getHeapUsage call.
        """
        return await self.client.send(method="Runtime.getHeapUsage", params=params, session_id=session_id)
    async def get_properties(self, params: getPropertiesParameters | None = None, session_id: str | None = None) -> getPropertiesReturns:
        """
    Returns properties of a given object. Object group of the result is inherited from the target object.    
        Args:
            params (getPropertiesParameters, optional): Parameters for the getProperties method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getPropertiesReturns: The result of the getProperties call.
        """
        return await self.client.send(method="Runtime.getProperties", params=params, session_id=session_id)
    async def global_lexical_scope_names(self, params: globalLexicalScopeNamesParameters | None = None, session_id: str | None = None) -> globalLexicalScopeNamesReturns:
        """
    Returns all let, const and class variables from global scope.    
        Args:
            params (globalLexicalScopeNamesParameters, optional): Parameters for the globalLexicalScopeNames method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    globalLexicalScopeNamesReturns: The result of the globalLexicalScopeNames call.
        """
        return await self.client.send(method="Runtime.globalLexicalScopeNames", params=params, session_id=session_id)
    async def query_objects(self, params: queryObjectsParameters | None = None, session_id: str | None = None) -> queryObjectsReturns:
        """
    No description available for queryObjects.    
        Args:
            params (queryObjectsParameters, optional): Parameters for the queryObjects method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    queryObjectsReturns: The result of the queryObjects call.
        """
        return await self.client.send(method="Runtime.queryObjects", params=params, session_id=session_id)
    async def release_object(self, params: releaseObjectParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Releases remote object with given id.    
        Args:
            params (releaseObjectParameters, optional): Parameters for the releaseObject method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the releaseObject call.
        """
        return await self.client.send(method="Runtime.releaseObject", params=params, session_id=session_id)
    async def release_object_group(self, params: releaseObjectGroupParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Releases all remote objects that belong to a given group.    
        Args:
            params (releaseObjectGroupParameters, optional): Parameters for the releaseObjectGroup method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the releaseObjectGroup call.
        """
        return await self.client.send(method="Runtime.releaseObjectGroup", params=params, session_id=session_id)
    async def run_if_waiting_for_debugger(self, params: runIfWaitingForDebuggerParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Tells inspected instance to run if it was waiting for debugger to attach.    
        Args:
            params (runIfWaitingForDebuggerParameters, optional): Parameters for the runIfWaitingForDebugger method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the runIfWaitingForDebugger call.
        """
        return await self.client.send(method="Runtime.runIfWaitingForDebugger", params=params, session_id=session_id)
    async def run_script(self, params: runScriptParameters | None = None, session_id: str | None = None) -> runScriptReturns:
        """
    Runs script with given id in a given context.    
        Args:
            params (runScriptParameters, optional): Parameters for the runScript method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    runScriptReturns: The result of the runScript call.
        """
        return await self.client.send(method="Runtime.runScript", params=params, session_id=session_id)
    async def set_async_call_stack_depth(self, params: setAsyncCallStackDepthParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables or disables async call stacks tracking.    
        Args:
            params (setAsyncCallStackDepthParameters, optional): Parameters for the setAsyncCallStackDepth method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAsyncCallStackDepth call.
        """
        return await self.client.send(method="Runtime.setAsyncCallStackDepth", params=params, session_id=session_id)
    async def set_custom_object_formatter_enabled(self, params: setCustomObjectFormatterEnabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setCustomObjectFormatterEnabled.    
        Args:
            params (setCustomObjectFormatterEnabledParameters, optional): Parameters for the setCustomObjectFormatterEnabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setCustomObjectFormatterEnabled call.
        """
        return await self.client.send(method="Runtime.setCustomObjectFormatterEnabled", params=params, session_id=session_id)
    async def set_max_call_stack_size_to_capture(self, params: setMaxCallStackSizeToCaptureParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setMaxCallStackSizeToCapture.    
        Args:
            params (setMaxCallStackSizeToCaptureParameters, optional): Parameters for the setMaxCallStackSizeToCapture method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setMaxCallStackSizeToCapture call.
        """
        return await self.client.send(method="Runtime.setMaxCallStackSizeToCapture", params=params, session_id=session_id)
    async def terminate_execution(self, params: terminateExecutionParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Terminate current or next JavaScript execution. Will cancel the termination when the outer-most script execution ends.    
        Args:
            params (terminateExecutionParameters, optional): Parameters for the terminateExecution method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the terminateExecution call.
        """
        return await self.client.send(method="Runtime.terminateExecution", params=params, session_id=session_id)
    async def add_binding(self, params: addBindingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    If executionContextId is empty, adds binding with the given name on the global objects of all inspected contexts, including those created later, bindings survive reloads. Binding function takes exactly one argument, this argument should be string, in case of any other input, function throws an exception. Each binding function call produces Runtime.bindingCalled notification.    
        Args:
            params (addBindingParameters, optional): Parameters for the addBinding method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the addBinding call.
        """
        return await self.client.send(method="Runtime.addBinding", params=params, session_id=session_id)
    async def remove_binding(self, params: removeBindingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    This method does not remove binding function from global object but unsubscribes current runtime agent from Runtime.bindingCalled notifications.    
        Args:
            params (removeBindingParameters, optional): Parameters for the removeBinding method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeBinding call.
        """
        return await self.client.send(method="Runtime.removeBinding", params=params, session_id=session_id)
    async def get_exception_details(self, params: getExceptionDetailsParameters | None = None, session_id: str | None = None) -> getExceptionDetailsReturns:
        """
    This method tries to lookup and populate exception details for a JavaScript Error object. Note that the stackTrace portion of the resulting exceptionDetails will only be populated if the Runtime domain was enabled at the time when the Error was thrown.    
        Args:
            params (getExceptionDetailsParameters, optional): Parameters for the getExceptionDetails method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getExceptionDetailsReturns: The result of the getExceptionDetails call.
        """
        return await self.client.send(method="Runtime.getExceptionDetails", params=params, session_id=session_id)