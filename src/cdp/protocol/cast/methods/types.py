"""CDP Cast Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

class enableParameters(TypedDict, total=False):
    presentationUrl: NotRequired[str]

class setSinkToUseParameters(TypedDict, total=True):
    sinkName: str
class startDesktopMirroringParameters(TypedDict, total=True):
    sinkName: str
class startTabMirroringParameters(TypedDict, total=True):
    sinkName: str
class stopCastingParameters(TypedDict, total=True):
    sinkName: str