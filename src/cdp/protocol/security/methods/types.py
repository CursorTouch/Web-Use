"""CDP Security Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple



class setIgnoreCertificateErrorsParameters(TypedDict, total=True):
    ignore: bool
    """If true, all certificate errors will be ignored."""