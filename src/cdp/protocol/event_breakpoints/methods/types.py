"""CDP EventBreakpoints Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

class setInstrumentationBreakpointParameters(TypedDict, total=True):
    eventName: str
    """Instrumentation name to stop on."""
class removeInstrumentationBreakpointParameters(TypedDict, total=True):
    eventName: str
    """Instrumentation name to stop on."""