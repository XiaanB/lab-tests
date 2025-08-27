# my_module.py

def safe_divide(a: float, b: float) -> float:
    """Divides a by b, returns 'inf' if b == 0."""
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')

def categorize_number(n: int) -> str:
    """Returns a category for the number."""
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    elif n % 2 == 0:
        return "even"
    else:
        return "odd"
