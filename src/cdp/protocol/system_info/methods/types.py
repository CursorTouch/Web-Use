"""CDP SystemInfo Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.system_info.types import GPUInfo
    from cdp.protocol.system_info.types import ProcessInfo


class getFeatureStateParameters(TypedDict, total=True):
    featureState: str

class getInfoReturns(TypedDict):
    gpu: GPUInfo
    """Information about the GPUs on the system."""
    modelName: str
    """A platform-dependent description of the model of the machine. On Mac OS, this is, for example, 'MacBookPro'. Will be the empty string if not supported."""
    modelVersion: str
    """A platform-dependent description of the version of the machine. On Mac OS, this is, for example, '10.1'. Will be the empty string if not supported."""
    commandLine: str
    """The command line string used to launch the browser. Will be the empty string if not supported."""
class getFeatureStateReturns(TypedDict):
    featureEnabled: bool
class getProcessInfoReturns(TypedDict):
    processInfo: List[ProcessInfo]
    """An array of process info blocks."""