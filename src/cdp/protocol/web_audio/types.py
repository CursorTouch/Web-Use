"""CDP WebAudio Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

GraphObjectId = str
"""An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in Web Audio API"""
ContextType = Literal['realtime','offline']
"""Enum of BaseAudioContext types"""
ContextState = Literal['suspended','running','closed','interrupted']
"""Enum of AudioContextState from the spec"""
NodeType = str
"""Enum of AudioNode types"""
ChannelCountMode = Literal['clamped-max','explicit','max']
"""Enum of AudioNode::ChannelCountMode from the spec"""
ChannelInterpretation = Literal['discrete','speakers']
"""Enum of AudioNode::ChannelInterpretation from the spec"""
ParamType = str
"""Enum of AudioParam types"""
AutomationRate = Literal['a-rate','k-rate']
"""Enum of AudioParam::AutomationRate from the spec"""
class ContextRealtimeData(TypedDict, total=True):
    """Fields in AudioContext that change in real-time."""
    currentTime: float
    """The current context time in second in BaseAudioContext."""
    renderCapacity: float
    """The time spent on rendering graph divided by render quantum duration, and multiplied by 100. 100 means the audio renderer reached the full capacity and glitch may occur."""
    callbackIntervalMean: float
    """A running mean of callback interval."""
    callbackIntervalVariance: float
    """A running variance of callback interval."""
class BaseAudioContext(TypedDict, total=True):
    """Protocol object for BaseAudioContext"""
    contextId: GraphObjectId
    contextType: ContextType
    contextState: ContextState
    callbackBufferSize: float
    """Platform-dependent callback buffer size."""
    maxOutputChannelCount: float
    """Number of output channels supported by audio hardware in use."""
    sampleRate: float
    """Context sample rate."""
    realtimeData: NotRequired[ContextRealtimeData]
class AudioListener(TypedDict, total=True):
    """Protocol object for AudioListener"""
    listenerId: GraphObjectId
    contextId: GraphObjectId
class AudioNode(TypedDict, total=True):
    """Protocol object for AudioNode"""
    nodeId: GraphObjectId
    contextId: GraphObjectId
    nodeType: NodeType
    numberOfInputs: float
    numberOfOutputs: float
    channelCount: float
    channelCountMode: ChannelCountMode
    channelInterpretation: ChannelInterpretation
class AudioParam(TypedDict, total=True):
    """Protocol object for AudioParam"""
    paramId: GraphObjectId
    nodeId: GraphObjectId
    contextId: GraphObjectId
    paramType: ParamType
    rate: AutomationRate
    defaultValue: float
    minValue: float
    maxValue: float