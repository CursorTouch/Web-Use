"""CDP HeadlessExperimental Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

class ScreenshotParams(TypedDict, total=False):
    """Encoding options for a screenshot."""
    format: NotRequired[Literal["jpeg", "png", "webp"]]
    """Image compression format (defaults to png)."""
    quality: NotRequired[int]
    """Compression quality from range [0..100] (jpeg and webp only)."""
    optimizeForSpeed: NotRequired[bool]
    """Optimize image encoding for speed, not for resulting size (defaults to false)"""