import pytest

def error_handling_numbers(user_input):
    valid = False
    while not valid:
        try:
            float(user_input)
            valid = True
            return user_input
        except ValueError:
            print("That is not a valid number, please enter a valid number")
            user_input = input()

def test_error_handling_numbers():
    assert error_handling_numbers() == float()