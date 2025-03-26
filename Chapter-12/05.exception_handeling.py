"""
There are many built-in exceptions which are raised in python when something goes 
wrong. 
Exception in python can be handled using a try statement. The code that handles the 
exception is written in the except clause.
"""

try:
    # Code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    # Handle the exception
    print(f"Error: {e}")
finally:
    # This block will always execute
    print("This block executes no matter what.")


# We can also specify the exception to catch like below:

try:
    # Code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # Handle the specific exception
    print(f"ZeroDivisionError: {e}")
except TypeError as e:
    # Handle another specific exception
    print(f"TypeError: {e}")
except Exception as e:
    # Handle any other exception
    print(f"General Exception: {e}")
