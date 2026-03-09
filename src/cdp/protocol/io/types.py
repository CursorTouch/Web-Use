"""CDP IO Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

StreamHandle = str
"""This is either obtained from another method or specified as blob:<uuid> where <uuid> is an UUID of a Blob."""