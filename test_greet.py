import pytest
from greet import greet


def test_default_greeting():
    assert greet("Alice") == "Hello, Alice!"


def test_shout():
    assert greet("Alice", shout=True) == "HELLO, ALICE!"


def test_empty_name_raises():
    with pytest.raises(ValueError):
        greet("")
