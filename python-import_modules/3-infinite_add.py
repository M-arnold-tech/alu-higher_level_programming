#!/usr/bin/python3
import sys


import sys


if __name__ == "__main__":
    total = 0  # Initialize the total sum

    # Loop through the command-line arguments, starting from index 1
    for arg in sys.argv[1:]:
        total += int(arg)  # Convert each argument to an integer

    print(total)  # Print the final total
