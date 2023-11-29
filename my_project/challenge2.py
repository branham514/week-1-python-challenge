def exactly_two_positive(a, b, c):
    positive_count = 0

    # Check each number and increment the positive_count if positive
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    # Check if exactly two numbers are positive
    return positive_count == 2

# Examples:
print(exactly_two_positive(2, 4, -3))  # Output: True
print(exactly_two_positive(-4, 6, 8))  # Output: True
print(exactly_two_positive(4, -6, 9))  # Output: True
print(exactly_two_positive(-4, 6, 0))  # Output: False
print(exactly_two_positive(4, 6, 10))  # Output: False
print(exactly_two_positive(-14, -3, -4))  # Output: False
