"""
Preview Formatter for Printcraft
"""

from typing import Any
from .themes import apply_theme
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def preview(obj: Any, max_items: int = 10, theme: str = "classic") -> None:
    """
    Print a compact preview of large data structures.

    Parameters:
    - obj: Python object (list, tuple, dict, etc.)
    - max_items: maximum number of items to display
    - theme: color theme ('classic', 'dark', 'minimal')
    """
    try:
        # Handle lists and tuples
        if isinstance(obj, (list, tuple)):
            length = len(obj)
            displayed = obj[:max_items]
            suffix = f", ... {length - max_items} more items ..." if length > max_items else ""
            opening = "[" if isinstance(obj, list) else "("
            closing = "]" if isinstance(obj, list) else ")"
            line = f"{opening}{', '.join(str(item) for item in displayed)}{suffix}{closing}"
            print(apply_theme(line, theme=theme))

        # Handle dicts
        elif isinstance(obj, dict):
            keys = list(obj.keys())
            length = len(keys)
            displayed_keys = keys[:max_items]
            suffix = f"... {length - max_items} more keys ..." if length > max_items else ""
            for key in displayed_keys:
                print(apply_theme(f"{key} : {obj[key]}", theme=theme))
            if suffix:
                print(apply_theme(suffix, theme=theme))

        # Fallback for other types
        else:
            print(apply_theme(str(obj), theme=theme))

    except Exception as e:
        print(f"[printcraft][preview] Error in preview: {e}")
