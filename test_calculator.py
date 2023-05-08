import pytest
from calculator import add

def test_addition1():
    assert add(2, 3) == 5

def test_addition2():
    assert add(0, 0) == 0

def test_addition3():
    assert add(-1, 1) == 0