#!/usr/bin/python3
def no_c(my_string):
    # Create an empty list to store the characters that are not 'c' or 'C'
    result = []

    # Iterate through each character in the input string
    for char in my_string:
        # Append the character to the result list if it's not 'c' or 'C'
        if char != 'c' and char != 'C':
            result.append(char)

    # Join the list into a new string and return it
    return ''.join(result)
