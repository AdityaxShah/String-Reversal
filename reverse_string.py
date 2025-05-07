"""
reverse_string.py

This script contains a simple function to reverse a given string in Python.
It demonstrates basic string manipulation and is suitable for beginners.

Author: Aditya Shah
Date: May 7, 2025
"""

def reverse_string(input_string):
    """
    Reverses the given string.

    Parameters:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    # Using Python slicing to reverse the string
    reversed_str = input_string[::-1]
    
    return reversed_str


if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    result = reverse_string(user_input)
    print(f"Reversed string: {result}")
