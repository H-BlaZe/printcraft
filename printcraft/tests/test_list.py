import pytest
from printcraft.list_formatter import plist

def test_plist_empty():
    try:
        plist([])
    except Exception:
        pytest.fail("plist raised exception on empty list")

def test_plist_basic():
    data = [1,2,3,4]
    try:
        plist(data)
    except Exception:
        pytest.fail("plist raised exception on valid list")

def test_plist_tuple():
    data = (1,2,3)
    try:
        plist(list(data))
    except Exception:
        pytest.fail("plist raised exception on tuple")
