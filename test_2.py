# test_2.py
from example_functions import reverse_string

# Test reversing normal strings
def test_normal_strings():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    print("test_normal_strings passed ✅")

# Test empty string
def test_empty_string():
    assert reverse_string("") == ""
    print("test_empty_string passed ✅")

# Test single character
def test_single_char():
    assert reverse_string("A") == "A"
    print("test_single_char passed ✅")

# Test strings with spaces and punctuation
def test_spaces_and_punct():
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"
    assert reverse_string("123 456") == "654 321"
    print("test_spaces_and_punct passed ✅")

# Optional: failing test (to see pytest report)
def test_fail():
    assert reverse_string("abc") == "abc"  # intentional fail
    print("test_fail ran ❌")
