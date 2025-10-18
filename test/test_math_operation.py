from src.math_operations import add, sub

def test_add():
    assert add(1, 2) == 3
    assert add(5, 7) == 12

def test_sub():
    assert sub(2, 1) == 1
    assert sub(9, 1) == 8