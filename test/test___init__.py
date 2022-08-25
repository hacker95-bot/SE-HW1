import pytest
from code import factorial


def test_negative_factorial():
    assert factorial(-1) == 1


def test_zero_factorial():
    assert factorial(0) == 1


@pytest.mark.parametrize("x,val", [
    (1, 1),
    (2, 2),
    (3, 6),
    (5, 120)
])
def test_positive_factorial(x, val):
    assert factorial(x) == val
