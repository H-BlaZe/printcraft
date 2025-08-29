import pytest
from printcraft.table_formatter import ptable, export_markdown, export_html

def test_ptable_empty():
    try:
        ptable([])
    except Exception:
        pytest.fail("ptable raised exception on empty list")

def test_ptable_basic():
    data = [{"id":1, "name":"Khan"}, {"id":2,"name":"Maya"}]
    try:
        ptable(data)
    except Exception:
        pytest.fail("ptable raised exception on valid data")

def test_export_markdown():
    data = [{"id":1, "name":"Khan"}, {"id":2,"name":"Maya"}]
    md = export_markdown(data)
    assert "| id | name |" in md

def test_export_html():
    data = [{"id":1, "name":"Khan"}]
    html = export_html(data)
    assert "<table" in html and "</table>" in html
