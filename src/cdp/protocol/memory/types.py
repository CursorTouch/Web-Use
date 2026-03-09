"""CDP Memory Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

PressureLevel = Literal['moderate','critical']
"""Memory pressure level."""
class SamplingProfileNode(TypedDict, total=True):
    """Heap profile sample."""
    size: float
    """Size of the sampled allocation."""
    total: float
    """Total bytes attributed to this sample."""
    stack: List[str]
    """Execution stack at the point of allocation."""
class SamplingProfile(TypedDict, total=True):
    """Array of heap profile samples."""
    samples: List[SamplingProfileNode]
    modules: List[Module]
class Module(TypedDict, total=True):
    """Executable module information"""
    name: str
    """Name of the module."""
    uuid: str
    """UUID of the module."""
    baseAddress: str
    """Base address where the module is loaded into memory. Encoded as a decimal or hexadecimal (0x prefixed) string."""
    size: float
    """Size of the module in bytes."""
class DOMCounter(TypedDict, total=True):
    """DOM object counter data."""
    name: str
    """Object name. Note: object names should be presumed volatile and clients should not expect the returned names to be consistent across runs."""
    count: int
    """Object count."""