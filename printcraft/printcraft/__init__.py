"""
Printcraft: A Python library for beautifully formatted printing of JSON,
tables, dicts, lists, tuples, and more.
"""

# Safe imports – so that even if one submodule has an error,
# the package doesn’t completely crash on import.
# Instead, missing features will be reported gracefully.

__version__ = "0.1.0"
__author__ = "Your Name"
__license__ = "MIT"

# Expose public API
try:
    from .json_formatter import pjson
except Exception as e:
    def pjson(*args, **kwargs):
        raise ImportError(f"printcraft.json_formatter could not be loaded:  ")

try:
    from .table_formatter import ptable, export_markdown, export_html
except Exception as e:
    def ptable(*args, **kwargs):
        raise ImportError(f"printcraft.table_formatter could not be loaded:  ")
    def export_markdown(*args, **kwargs):
        raise ImportError(f"printcraft.table_formatter could not be loaded:  ")
    def export_html(*args, **kwargs):
        raise ImportError(f"printcraft.table_formatter could not be loaded:  ")

try:
    from .dict_formatter import pdict
except Exception as e:
    def pdict(*args, **kwargs):
        raise ImportError(f"printcraft.dict_formatter could not be loaded:  ")

try:
    from .list_formatter import plist
except Exception as e:
    def plist(*args, **kwargs):
        raise ImportError(f"printcraft.list_formatter could not be loaded:  ")

try:
    from .preview import preview
except Exception as e:
    def preview(*args, **kwargs):
        raise ImportError(f"printcraft.preview could not be loaded:  ")

try:
    from .core import pcraft
except Exception as e:
    def pcraft(*args, **kwargs):
        raise ImportError(f"printcraft.core could not be loaded:  ")

__all__ = [
    "pjson",
    "ptable",
    "pdict",
    "plist",
    "preview",
    "pcraft",
    "export_markdown",
    "export_html",
]
