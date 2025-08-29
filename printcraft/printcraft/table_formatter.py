"""
Table Formatter for Printcraft
"""

from typing import List, Dict, Any
from .themes import apply_theme
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def ptable(data, headers=None, style="ascii", color=False):
    """
    Pretty print a table in the terminal.
    Supports ascii and unicode styles.
    """
    if not data:
        print("(empty table)")
        return

    # If dicts, extract headers
    if isinstance(data[0], dict):
        if headers is None:
            headers = list(data[0].keys())
        rows = [[str(row.get(h, "")) for h in headers] for row in data]
    else:
        if headers is None:
            headers = [f"col{i}" for i in range(len(data[0]))]
        rows = [[str(x) for x in row] for row in data]

    # Compute column widths
    col_widths = [max(len(str(h)), max(len(r[i]) for r in rows)) for i, h in enumerate(headers)]

    # Border characters
    if style == "ascii":
        corner, horiz, vert = "+", "-", "|"
    else:  # unicode
        corner, horiz, vert = "┼", "─", "│"

    # Build line separator
    sep = corner + corner.join(horiz * (w + 2) for w in col_widths) + corner

    # Print header
    print(sep)
    header_row = vert + vert.join(f" {h:<{w}} " for h, w in zip(headers, col_widths)) + vert
    print(header_row)
    print(sep)

    # Print rows
    for idx, row in enumerate(rows, start=1):
        cells = []
        for i, w in enumerate(col_widths):
            cell = f"{row[i]:<{w}}"
            if color:
                # Example: colorize first col with yellow numbers
                if i == 0:
                    cell = f"\033[1;33m{cell}\033[0m"
            cells.append(f" {cell} ")
        print(vert + vert.join(cells) + vert)
    print(sep)


def export_markdown(data, headers=None):
    """
    Export table as Markdown format string.
    """
    if not data:
        return ""

    if isinstance(data[0], dict):
        if headers is None:
            headers = list(data[0].keys())
        rows = [[str(row.get(h, "")) for h in headers] for row in data]
    else:
        if headers is None:
            headers = [f"col{i}" for i in range(len(data[0]))]
        rows = [[str(x) for x in row] for row in data]

    # Header row
    header_line = "| " + " | ".join(headers) + " |"
    sep_line = "| " + " | ".join("---" for _ in headers) + " |"

    # Data rows
    row_lines = ["| " + " | ".join(r) + " |" for r in rows]

    return "\n".join([header_line, sep_line] + row_lines)


def export_html(data: List[Dict[str, Any]]) -> str:
    """Export list of dicts as HTML table"""
    try:
        if not data:
            return "<table></table>"
        columns = list(data[0].keys())
        html = "<table border='1'>\n<tr>" + "".join(f"<th>{col}</th>" for col in columns) + "</tr>\n"
        for row in data:
            html += "<tr>" + "".join(f"<td>{row.get(col, '')}</td>" for col in columns) + "</tr>\n"
        html += "</table>"
        return html
    except Exception as e:
        return f"[printcraft][export_html] Error: {e}"
