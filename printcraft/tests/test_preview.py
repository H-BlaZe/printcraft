import pytest
from printcraft.preview import preview

def test_preview_list():
    data = list(range(20))
    try:
        preview(data, max_items=5)
    except Exception:
        pytest.fail("preview failed on list")

def test_preview_dict():
    data = {f"key{i}": i for i in range(20)}
    try:
        preview(data, max_items=5)
    except Exception:
        pytest.fail("preview failed on dict")

def test_preview_other():
    data = "Some string"
    try:
        preview(data)
    except Exception:
        pytest.fail("preview failed on other object")
