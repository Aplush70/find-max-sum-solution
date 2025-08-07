"""
Assumptions:
- Each digit in the string is treated as a standalone number (e.g. '36' → 3 + 6).
- Input list can be up to 10 strings, each up to 12 characters.
- Strings may contain letters, digits, or both.
- Strings with no digits contribute 0 to the max comparison.
- Only the largest digit sum is returned (not the string that had it).
"""

def max_digit_sum(strings):
    """
    Given a list of alphanumeric strings, returns the maximum sum of digits in any string.
    Each digit is treated as a single-digit number.
    """
    max_sum = 0

    for s in strings:
        digit_sum = sum(int(c) for c in s if c.isdigit())
        max_sum = max(max_sum, digit_sum)

    return max_sum


