# test_1.py
from example_functions import is_even, square

# Passing tests
def test_positive_even():
    assert is_even(2) is True
    assert is_even(10) is True
    print("test_positive_even passed ✅")

def test_positive_odd():
    assert is_even(3) is False
    assert is_even(17) is False
    print("test_positive_odd passed ✅")

def test_zero():
    assert is_even(0) is True
    print("test_zero passed ✅")

def test_negative():
    assert is_even(-2) is True
    assert is_even(-7) is False
    print("test_negative passed ✅")

# Failing tests (intentional)
def test_fail_even():
    assert is_even(3) is True  # This should fail
    print("test_fail_even ran ❌")

def test_fail_square():
    assert square(3) == 10  # This should fail
    print("test_fail_square ran ❌")
