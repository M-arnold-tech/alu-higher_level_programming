#!/usr/bin/python3


def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:  # Check if char is lowercase
            char = chr(ord(char) - 32)  # Convert to uppercase
        print("{}".format(char), end="")
    print()  # Print a newline at the end
