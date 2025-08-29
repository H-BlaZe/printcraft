"""
Utility functions for Printcraft
"""

from typing import Any

def is_iterable(obj: Any) -> bool:
    """Check if object is iterable (list, tuple, dict)"""
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def safe_str(obj: Any, max_len: int = 100) -> str:
    """
    Convert object to string safely.
    Truncate if longer than max_len.
    """
    try:
        s = str(obj)
        if len(s) > max_len:
            return s[:max_len] + "..."
        return s
    except Exception:
        return f"<Unrepresentable object: {type(obj).__name__}>"

def truncate_list(lst: list, max_items: int = 10) -> list:
    """
    Return a truncated version of a list with a note if truncated.
    """
    try:
        if len(lst) > max_items:
            return lst[:max_items] + [f"... {len(lst) - max_items} more items ..."]
        return lst
    except Exception:
        return ["<Error truncating list>"]

def truncate_dict(d: dict, max_items: int = 10) -> dict:
    """
    Return a truncated version of a dict with a note if truncated.
    """
    try:
        if len(d) > max_items:
            keys = list(d.keys())[:max_items]
            truncated = {k: d[k] for k in keys}
            truncated[f"... {len(d) - max_items} more keys ..."] = ""
            return truncated
        return d
    except Exception:
        return {"<Error truncating dict>": ""}
