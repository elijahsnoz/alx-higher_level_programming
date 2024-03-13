#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s

    new_str = s[:n] + s[n+1:]
    return new_str
