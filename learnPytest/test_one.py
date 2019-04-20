"""
命令行执行 pytest -v test_one.py
"""
import pytest

def test_passing():
    assert (1,2,3) == (1,3,3)
    
def test_passing2():
    assert "a" in "def"

def test_passing3():
    assert True == True
