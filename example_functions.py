# example_functions.py

def is_even(number: int) -> bool:
    return number % 2 == 0

def square(x: int) -> int:
    return x * x


def reverse_string(s: str) -> str:
    """
    Returns the reverse of the given string.
    """
    return s[::-1]
