#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    # Initialize a variable to store the sum
    total = 0
    for arg in arguments:
        total += int(arg)
    print(total)
