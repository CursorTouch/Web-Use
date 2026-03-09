"""CDP Inspector Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

class detachedEvent(TypedDict, total=True):
    reason: str
    """The reason why connection has been terminated."""
class targetCrashedEvent(TypedDict, total=True):
    pass
class targetReloadedAfterCrashEvent(TypedDict, total=True):
    pass
class workerScriptLoadedEvent(TypedDict, total=True):
    pass