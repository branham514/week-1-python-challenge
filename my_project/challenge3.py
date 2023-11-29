def solve(s):
    vowels = "aeiou"
    consonant_values = []

    current_consonant_value = 0

    for char in s:
        if char not in vowels:
            current_consonant_value += ord(char) - ord('a') + 1
        else:
            if current_consonant_value > 0:
                consonant_values.append(current_consonant_value)
                current_consonant_value = 0

    # Check for the last consonant substring
    if current_consonant_value > 0:
        consonant_values.append(current_consonant_value)

    
    return max(consonant_values, default=0)

print(solve("zodiacs"))   # Output: 26
print(solve("strength"))  # Output: 57
