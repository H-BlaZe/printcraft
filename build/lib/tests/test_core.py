import pytest
from printcraft.core import pcraft

def test_pcraft_dict():
    data = {"name": "Khan"}
    try:
        pcraft(data)
    except Exception:
        pytest.fail("pcraft failed on dict")

def test_pcraft_list_of_dicts():
    data = [{"id":1,"name":"Khan"}, {"id":2,"name":"Maya"}]
    try:
        pcraft(data)
    except Exception:
        pytest.fail("pcraft failed on list of dicts")

def test_pcraft_list():
    data = [1,2,3]
    try:
        pcraft(data)
    except Exception:
        pytest.fail("pcraft failed on list")

def test_pcraft_tuple():
    data = (1,2,3)
    try:
        pcraft(data)
    except Exception:
        pytest.fail("pcraft failed on tuple")

def test_pcraft_json_string():
    data = '{"name":"Khan"}'
    try:
        pcraft(data)
    except Exception:
        pytest.fail("pcraft failed on JSON string")
