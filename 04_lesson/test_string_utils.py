import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):  
    assert string_utils.capitalize(input_str) == expected  


@pytest.mark.negative_test 
@pytest.mark.xfail 
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("Already", "Already"),  
])
def test_capitalize_negative(input_str, expected):  
    assert string_utils.capitalize(input_str) == expected  



@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   hello world", "hello world"),
    ("   python", "python"),
    ("  test", "test"),  
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative_test 
@pytest.mark.xfail
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),  
    ("skypro", "skypro"),  
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected



@pytest.mark.positive_test
@pytest.mark.parametrize("string, substring, expected", [
    ("skypro", "sky", True),
    ("hello world", "world", True),
    ("python", "th", True),
])
def test_contains_positive(string, substring, expected):
    assert string_utils.contains(string, substring) == expected


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize("string, substring, expected", [
    ("hello", "x", False),
    ("", "test", False),
    ("skypro", "proo", False),
])
def test_contains_negative(string, substring, expected):
    assert string_utils.contains(string, substring) == expected



@pytest.mark.positive_test
@pytest.mark.parametrize("string, old, expected", [
    ("SkyPro", "Sky", "Pro"),
    ("hello world", "hello", " world"),
    ("aabbcc", "bb", "aacc"),
])
def test_delete_symbol_positive(string, old, expected):
    assert string_utils.delete_symbol(string, old) == expected


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize("string, old, expected", [
    ("hello", "test", "hello"),
    ("", "old", ""),
    ("test", "t", "es"),
])
def test_delete_symbol_negative(string, old, expected):
    assert string_utils.delete_symbol(string, old) == expected