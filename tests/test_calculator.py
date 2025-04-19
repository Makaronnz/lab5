import pytest
from calculator import add, subtract, multiply, divide

@pytest.fixture
def calculator_values():
    return {"a": 10, "b": 5}

def test_add_with_fixture(calculator_values):
    assert add(calculator_values["a"], calculator_values["b"]) == 15

def test_subtract_with_fixture(calculator_values):
    assert subtract(calculator_values["a"], calculator_values["b"]) == 5

def test_multiply_with_fixture(calculator_values):
    assert multiply(calculator_values["a"], calculator_values["b"]) == 50

def test_divide_with_fixture(calculator_values):
    assert divide(calculator_values["a"], calculator_values["b"]) == 2

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (0, 0, 0),
    (1, 5, -4),
    (-5, -3, -2)
])
def test_subtract_parametrized(a, b, expected):
    assert subtract(a, b) == expected

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 5) == -4
    assert subtract(-1, -1) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 3) == -3
    assert multiply(-1, -1) == 1


def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-1, 1) == -1

    with pytest.raises(ValueError):
        divide(5, 0)