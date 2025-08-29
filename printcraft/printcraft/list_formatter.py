"""
List/Tuple Formatter for Printcraft
"""

from typing import List, Any
from .themes import apply_theme
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def plist(data: List[Any], theme: str = "classic") -> None:
    """
    Print a list or tuple in an aligned, readable format.

    Parameters:
    - data: list or tuple
    - theme: color theme ('classic', 'dark', 'minimal')
    """
    try:
        if not data:
            print("[printcraft][plist] Empty list/tuple")
            return

        is_tuple = isinstance(data, tuple)
        opening = "(" if is_tuple else "["
        closing = ")" if is_tuple else "]"

        # Build formatted lines
        lines = [opening]
        for item in data:
            lines.append(f"  {item},")
        lines.append(closing)

        for line in lines:
            print(apply_theme(line, theme=theme))

    except Exception as e:
        print(f"[printcraft][plist] Error printing list/tuple: {e}")
