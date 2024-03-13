#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s

    new_str = ""
    for i in range(len(s)):
        if i != n:
            new_str += s[i]

    return new_str

# Example usage:
original_str = "Hello"
position_to_remove = 2
new_str = remove_char_at(original_str, position_to_remove)
print(new_str)  # Output: Helo
