import pytest
from app import TestMe

def test_server():
    assert TestMe().take_five() == 5

def test_port():
    assert TestMe().port() == 8000
