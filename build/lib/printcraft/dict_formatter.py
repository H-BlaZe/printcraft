"""
Dictionary Formatter for Printcraft
"""

from typing import Dict, Any
from .themes import apply_theme
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def pdict(data: Dict[str, Any], theme: str = "classic") -> None:
    """
    Print a dictionary with aligned keys and values.

    Parameters:
    - data: dictionary to print
    - theme: color theme ('classic', 'dark', 'minimal')
    """
    try:
        if not data:
            print("[printcraft][pdict] Empty dictionary")
            return

        # Determine max key length for alignment
        max_key_len = max(len(str(key)) for key in data.keys())

        for key, value in data.items():
            line = f"{str(key):{max_key_len}} : {value}"
            print(apply_theme(line, theme=theme))

    except Exception as e:
        print(f"[printcraft][pdict] Error printing dictionary: {e}")
