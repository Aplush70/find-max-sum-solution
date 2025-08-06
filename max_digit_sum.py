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

if __name__ == "__main__":
    test_input = ["abc123", "456", "xyz36"]
    print(max_digit_sum(test_input))  # Should print 15
