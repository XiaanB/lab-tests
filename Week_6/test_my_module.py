# test_my_module.py

import pytest
from my_module import safe_divide, categorize_number

@pytest.mark.parametrize(
    "a,b,expected", [
        (6, 2, 3.0),
        (5, 0, float('inf')),
        (-10, -2, 5.0),
        (0, 5, 0.0)
    ]
)
def test_safe_divide(a, b, expected):
    assert safe_divide(a, b) == expected

@pytest.mark.parametrize(
    "n,expected", [
        (-5, "negative"),
        (0, "zero"),
        (2, "even"),
        (7, "odd")
    ]
)
def test_categorize_number(n, expected):
    assert categorize_number(n) == expected
