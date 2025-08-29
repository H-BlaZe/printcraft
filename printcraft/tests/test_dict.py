import pytest
from printcraft.dict_formatter import pdict

def test_pdict_empty():
    try:
        pdict({})
    except Exception:
        pytest.fail("pdict raised exception on empty dict")

def test_pdict_basic():
    data = {"name": "Khan", "age": 23}
    try:
        pdict(data)
    except Exception:
        pytest.fail("pdict raised exception on valid dict")
