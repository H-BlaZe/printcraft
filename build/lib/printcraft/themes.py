"""
Theme and color utilities for Printcraft
"""

from colorama import Fore, Style, Back, init

# Initialize colorama
init(autoreset=True)

# Define theme colors
THEMES = {
    "classic": {
        "key": Fore.CYAN + Style.BRIGHT,
        "string": Fore.GREEN,
        "number": Fore.YELLOW,
        "boolean": Fore.MAGENTA,
        "reset": Style.RESET_ALL,
    },
    "dark": {
        "key": Fore.LIGHTBLUE_EX + Style.BRIGHT,
        "string": Fore.LIGHTGREEN_EX,
        "number": Fore.LIGHTYELLOW_EX,
        "boolean": Fore.LIGHTMAGENTA_EX,
        "reset": Style.RESET_ALL,
    },
    "minimal": {
        "key": "",
        "string": "",
        "number": "",
        "boolean": "",
        "reset": "",
    },
}

def apply_theme(text: str, theme: str = "classic") -> str:
    """
    Apply colors to a string based on the theme.
    Currently applies simplistic coloring:
    - JSON keys
    - Numbers
    - Booleans
    """
    colors = THEMES.get(theme, THEMES["classic"])
    result = text

    try:
        # Color JSON-style keys (e.g., "key": )
        import re
        # Keys in quotes followed by colon
        result = re.sub(r'\"(.*?)\"\s*:', lambda m: f"{colors['key']}\"{m.group(1)}\"{colors['reset']}:", result)
        # Numbers
        result = re.sub(r'\b(\d+(\.\d+)?)\b', lambda m: f"{colors['number']}{m.group(1)}{colors['reset']}", result)
        # Booleans
        result = re.sub(r'\b(True|False)\b', lambda m: f"{colors['boolean']}{m.group(1)}{colors['reset']}", result)
    except Exception:
        # If anything fails, return unmodified text
        return text

    return result
