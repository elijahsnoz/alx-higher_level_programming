#!/usr/bin/python3
def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' and ':' characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']
    result = ''
    for char in text:
        result += char
        if char in punctuation_chars:
            print(result.strip())
            print()
            result = ''
    if result.strip():
        print(result.strip())
