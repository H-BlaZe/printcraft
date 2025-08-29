import pytest
from printcraft.json_formatter import pjson, is_json_string

def test_valid_json_string():
    json_str = '{"name": "Khan", "age": 23}'
    assert is_json_string(json_str) is True

def test_invalid_json_string():
    json_str = '{"name": "Khan", "age": 23'
    assert is_json_string(json_str) is False

def test_pjson_dict():
    data = {"name": "Maya", "age": 25}
    try:
        pjson(data)
    except Exception:
        pytest.fail("pjson raised exception on valid dict")

def test_pjson_json_string():
    data = '{"name": "Khan", "age": 23}'
    try:
        pjson(data)
    except Exception:
        pytest.fail("pjson raised exception on valid JSON string")
