#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False

# Example usage
if __name__ == "__main__":
    print(safe_print_integer(5))  # True
    print(safe_print_integer("hello"))  # False
