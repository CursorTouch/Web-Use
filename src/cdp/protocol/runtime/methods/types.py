"""CDP Runtime Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.runtime.types import CallArgument
    from cdp.protocol.runtime.types import ExceptionDetails
    from cdp.protocol.runtime.types import ExecutionContextId
    from cdp.protocol.runtime.types import InternalPropertyDescriptor
    from cdp.protocol.runtime.types import PrivatePropertyDescriptor
    from cdp.protocol.runtime.types import PropertyDescriptor
    from cdp.protocol.runtime.types import RemoteObject
    from cdp.protocol.runtime.types import RemoteObjectId
    from cdp.protocol.runtime.types import ScriptId
    from cdp.protocol.runtime.types import SerializationOptions
    from cdp.protocol.runtime.types import TimeDelta

class awaitPromiseParameters(TypedDict, total=True):
    promiseObjectId: RemoteObjectId
    """Identifier of the promise."""
    returnByValue: NotRequired[bool]
    """Whether the result is expected to be a JSON object that should be sent by value."""
    generatePreview: NotRequired[bool]
    """Whether preview should be generated for the result."""
class callFunctionOnParameters(TypedDict, total=True):
    functionDeclaration: str
    """Declaration of the function to call."""
    objectId: NotRequired[RemoteObjectId]
    """Identifier of the object to call function on. Either objectId or executionContextId should be specified."""
    arguments: NotRequired[List[CallArgument]]
    """Call arguments. All call arguments must belong to the same JavaScript world as the target object."""
    silent: NotRequired[bool]
    """In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides setPauseOnException state."""
    returnByValue: NotRequired[bool]
    """Whether the result is expected to be a JSON object which should be sent by value. Can be overriden by serializationOptions."""
    generatePreview: NotRequired[bool]
    """Whether preview should be generated for the result."""
    userGesture: NotRequired[bool]
    """Whether execution should be treated as initiated by user in the UI."""
    awaitPromise: NotRequired[bool]
    """Whether execution should await for resulting value and return once awaited promise is resolved."""
    executionContextId: NotRequired[ExecutionContextId]
    """Specifies execution context which global object will be used to call function on. Either executionContextId or objectId should be specified."""
    objectGroup: NotRequired[str]
    """Symbolic group name that can be used to release multiple objects. If objectGroup is not specified and objectId is, objectGroup will be inherited from object."""
    throwOnSideEffect: NotRequired[bool]
    """Whether to throw an exception if side effect cannot be ruled out during evaluation."""
    uniqueContextId: NotRequired[str]
    """An alternative way to specify the execution context to call function on. Compared to contextId that may be reused across processes, this is guaranteed to be system-unique, so it can be used to prevent accidental function call in context different than intended (e.g. as a result of navigation across process boundaries). This is mutually exclusive with executionContextId."""
    serializationOptions: NotRequired[SerializationOptions]
    """Specifies the result serialization. If provided, overrides generatePreview and returnByValue."""
class compileScriptParameters(TypedDict, total=True):
    expression: str
    """Expression to compile."""
    sourceURL: str
    """Source url to be set for the script."""
    persistScript: bool
    """Specifies whether the compiled script should be persisted."""
    executionContextId: NotRequired[ExecutionContextId]
    """Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page."""



class evaluateParameters(TypedDict, total=True):
    expression: str
    """Expression to evaluate."""
    objectGroup: NotRequired[str]
    """Symbolic group name that can be used to release multiple objects."""
    includeCommandLineAPI: NotRequired[bool]
    """Determines whether Command Line API should be available during the evaluation."""
    silent: NotRequired[bool]
    """In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides setPauseOnException state."""
    contextId: NotRequired[ExecutionContextId]
    """Specifies in which execution context to perform evaluation. If the parameter is omitted the evaluation will be performed in the context of the inspected page. This is mutually exclusive with uniqueContextId, which offers an alternative way to identify the execution context that is more reliable in a multi-process environment."""
    returnByValue: NotRequired[bool]
    """Whether the result is expected to be a JSON object that should be sent by value."""
    generatePreview: NotRequired[bool]
    """Whether preview should be generated for the result."""
    userGesture: NotRequired[bool]
    """Whether execution should be treated as initiated by user in the UI."""
    awaitPromise: NotRequired[bool]
    """Whether execution should await for resulting value and return once awaited promise is resolved."""
    throwOnSideEffect: NotRequired[bool]
    """Whether to throw an exception if side effect cannot be ruled out during evaluation. This implies disableBreaks below."""
    timeout: NotRequired[TimeDelta]
    """Terminate execution after timing out (number of milliseconds)."""
    disableBreaks: NotRequired[bool]
    """Disable breakpoints during execution."""
    replMode: NotRequired[bool]
    """Setting this flag to true enables let re-declaration and top-level await. Note that let variables can only be re-declared if they originate from replMode themselves."""
    allowUnsafeEvalBlockedByCSP: NotRequired[bool]
    """The Content Security Policy (CSP) for the target might block 'unsafe-eval' which includes eval(), Function(), setTimeout() and setInterval() when called with non-callable arguments. This flag bypasses CSP for this evaluation and allows unsafe-eval. Defaults to true."""
    uniqueContextId: NotRequired[str]
    """An alternative way to specify the execution context to evaluate in. Compared to contextId that may be reused across processes, this is guaranteed to be system-unique, so it can be used to prevent accidental evaluation of the expression in context different than intended (e.g. as a result of navigation across process boundaries). This is mutually exclusive with contextId."""
    serializationOptions: NotRequired[SerializationOptions]
    """Specifies the result serialization. If provided, overrides generatePreview and returnByValue."""


class getPropertiesParameters(TypedDict, total=True):
    objectId: RemoteObjectId
    """Identifier of the object to return properties for."""
    ownProperties: NotRequired[bool]
    """If true, returns properties belonging only to the element itself, not to its prototype chain."""
    accessorPropertiesOnly: NotRequired[bool]
    """If true, returns accessor properties (with getter/setter) only; internal properties are not returned either."""
    generatePreview: NotRequired[bool]
    """Whether preview should be generated for the results."""
    nonIndexedPropertiesOnly: NotRequired[bool]
    """If true, returns non-indexed properties only."""
class globalLexicalScopeNamesParameters(TypedDict, total=False):
    executionContextId: NotRequired[ExecutionContextId]
    """Specifies in which execution context to lookup global scope variables."""
class queryObjectsParameters(TypedDict, total=True):
    prototypeObjectId: RemoteObjectId
    """Identifier of the prototype to return objects for."""
    objectGroup: NotRequired[str]
    """Symbolic group name that can be used to release the results."""
class releaseObjectParameters(TypedDict, total=True):
    objectId: RemoteObjectId
    """Identifier of the object to release."""
class releaseObjectGroupParameters(TypedDict, total=True):
    objectGroup: str
    """Symbolic object group name."""

class runScriptParameters(TypedDict, total=True):
    scriptId: ScriptId
    """Id of the script to run."""
    executionContextId: NotRequired[ExecutionContextId]
    """Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page."""
    objectGroup: NotRequired[str]
    """Symbolic group name that can be used to release multiple objects."""
    silent: NotRequired[bool]
    """In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides setPauseOnException state."""
    includeCommandLineAPI: NotRequired[bool]
    """Determines whether Command Line API should be available during the evaluation."""
    returnByValue: NotRequired[bool]
    """Whether the result is expected to be a JSON object which should be sent by value."""
    generatePreview: NotRequired[bool]
    """Whether preview should be generated for the result."""
    awaitPromise: NotRequired[bool]
    """Whether execution should await for resulting value and return once awaited promise is resolved."""
class setAsyncCallStackDepthParameters(TypedDict, total=True):
    maxDepth: int
    """Maximum depth of async call stacks. Setting to 0 will effectively disable collecting async call stacks (default)."""
class setCustomObjectFormatterEnabledParameters(TypedDict, total=True):
    enabled: bool
class setMaxCallStackSizeToCaptureParameters(TypedDict, total=True):
    size: int

class addBindingParameters(TypedDict, total=True):
    name: str
    executionContextId: NotRequired[ExecutionContextId]
    """If specified, the binding would only be exposed to the specified execution context. If omitted and executionContextName is not set, the binding is exposed to all execution contexts of the target. This parameter is mutually exclusive with executionContextName. Deprecated in favor of executionContextName due to an unclear use case and bugs in implementation (crbug.com/1169639). executionContextId will be removed in the future."""
    executionContextName: NotRequired[str]
    """If specified, the binding is exposed to the executionContext with matching name, even for contexts created after the binding is added. See also ExecutionContext.name and worldName parameter to Page.addScriptToEvaluateOnNewDocument. This parameter is mutually exclusive with executionContextId."""
class removeBindingParameters(TypedDict, total=True):
    name: str
class getExceptionDetailsParameters(TypedDict, total=True):
    errorObjectId: RemoteObjectId
    """The error object for which to resolve the exception details."""
class awaitPromiseReturns(TypedDict):
    result: RemoteObject
    """Promise result. Will contain rejected value if promise was rejected."""
    exceptionDetails: ExceptionDetails
    """Exception details if stack strace is available."""
class callFunctionOnReturns(TypedDict):
    result: RemoteObject
    """Call result."""
    exceptionDetails: ExceptionDetails
    """Exception details."""
class compileScriptReturns(TypedDict):
    scriptId: ScriptId
    """Id of the script."""
    exceptionDetails: ExceptionDetails
    """Exception details."""



class evaluateReturns(TypedDict):
    result: RemoteObject
    """Evaluation result."""
    exceptionDetails: ExceptionDetails
    """Exception details."""
class getIsolateIdReturns(TypedDict):
    id: str
    """The isolate id."""
class getHeapUsageReturns(TypedDict):
    usedSize: float
    """Used JavaScript heap size in bytes."""
    totalSize: float
    """Allocated JavaScript heap size in bytes."""
    embedderHeapUsedSize: float
    """Used size in bytes in the embedder's garbage-collected heap."""
    backingStorageSize: float
    """Size in bytes of backing storage for array buffers and external strings."""
class getPropertiesReturns(TypedDict):
    result: List[PropertyDescriptor]
    """Object properties."""
    internalProperties: List[InternalPropertyDescriptor]
    """Internal object properties (only of the element itself)."""
    privateProperties: List[PrivatePropertyDescriptor]
    """Object private properties."""
    exceptionDetails: ExceptionDetails
    """Exception details."""
class globalLexicalScopeNamesReturns(TypedDict):
    names: List[str]
class queryObjectsReturns(TypedDict):
    objects: RemoteObject
    """Array with objects."""



class runScriptReturns(TypedDict):
    result: RemoteObject
    """Run result."""
    exceptionDetails: ExceptionDetails
    """Exception details."""






class getExceptionDetailsReturns(TypedDict):
    exceptionDetails: ExceptionDetails