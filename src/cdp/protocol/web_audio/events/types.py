"""CDP WebAudio Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.web_audio.types import AudioListener
    from cdp.protocol.web_audio.types import AudioNode
    from cdp.protocol.web_audio.types import AudioParam
    from cdp.protocol.web_audio.types import BaseAudioContext
    from cdp.protocol.web_audio.types import GraphObjectId

class contextCreatedEvent(TypedDict, total=True):
    context: BaseAudioContext
class contextWillBeDestroyedEvent(TypedDict, total=True):
    contextId: GraphObjectId
class contextChangedEvent(TypedDict, total=True):
    context: BaseAudioContext
class audioListenerCreatedEvent(TypedDict, total=True):
    listener: AudioListener
class audioListenerWillBeDestroyedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    listenerId: GraphObjectId
class audioNodeCreatedEvent(TypedDict, total=True):
    node: AudioNode
class audioNodeWillBeDestroyedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    nodeId: GraphObjectId
class audioParamCreatedEvent(TypedDict, total=True):
    param: AudioParam
class audioParamWillBeDestroyedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    nodeId: GraphObjectId
    paramId: GraphObjectId
class nodesConnectedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]
    destinationInputIndex: NotRequired[float]
class nodesDisconnectedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]
    destinationInputIndex: NotRequired[float]
class nodeParamConnectedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]
class nodeParamDisconnectedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]