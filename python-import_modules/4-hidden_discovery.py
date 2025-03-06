#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    # Get all names from the hidden_4 module
    names = dir(hidden_4)

    # Filter and sort names that do not start with '__'
    filtered_names = [name for name in names if not name.startswith("__")]
    filtered_names.sort()

    # Print each nme on a new line
    for name in filtered_names:
        print(name)
