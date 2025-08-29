"""
Core module for Printcraft: Auto-detection printing.
"""

from typing import Any
from .json_formatter import pjson, is_json_string
from .table_formatter import ptable, export_markdown, export_html
from .dict_formatter import pdict
from .list_formatter import plist
from .preview import preview

def pcraft(obj: Any, **kwargs):
    """
    Auto-detect the type of object and print it in the best format.
    
    Parameters:
    - obj: Any Python object (dict, list, tuple, JSON string, etc.)
    - kwargs: Optional parameters to pass to the specific formatter.
    
    Usage:
    >>> pcraft([{"id": 1, "name": "Khan"}])
    >>> pcraft({"username": "afaq"})
    >>> pcraft('[{"id":1,"name":"Khan"}]')
    """
    try:
        # JSON string detection
        if isinstance(obj, str) and is_json_string(obj):
            pjson(obj, **kwargs)
        # Dictionary
        elif isinstance(obj, dict):
            pdict(obj, **kwargs)
        # List of dicts -> table
        elif isinstance(obj, list):
            # Check if list of dicts (table)
            if obj and all(isinstance(i, dict) for i in obj):
                ptable(obj, **kwargs)
            else:
                plist(obj, **kwargs)
        # Tuple -> treat as list
        elif isinstance(obj, tuple):
            plist(list(obj), **kwargs)
        # Fallback -> preview
        else:
            preview(obj, **kwargs)
    except Exception as e:
        print(f"[printcraft] Error in pcraft: {e}")
