"""
JSON Formatter for Printcraft
"""

import json
from typing import Any
from .themes import apply_theme
from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

def is_json_string(s: str) -> bool:
    """Check if the string is valid JSON"""
    try:
        json.loads(s)
        return True
    except Exception:
        return False

def pjson(obj: Any, indent: int = 2, theme: str = "classic") -> None:
    """
    Pretty-print JSON with color highlighting.

    Parameters:
    - obj: dict, list, or JSON string
    - indent: number of spaces for indentation
    - theme: color theme ('classic', 'dark', 'minimal')
    """
    try:
        # If string -> parse JSON
        if isinstance(obj, str):
            data = json.loads(obj)
        else:
            data = obj

        # Convert to formatted JSON string
        json_str = json.dumps(data, indent=indent, ensure_ascii=False)
        
        # Apply colors using theme
        colored_json = apply_theme(json_str, theme=theme)
        
        print(colored_json)

    except Exception as e:
        print(f"[printcraft][pjson] Error formatting JSON: {e}")
