try:
    a = int("Enter a number: ")
    print(a)
except ValueError as e:
    print(f"ValueError: {e}")
except TypeError as e:
    print(f"TypeError: {e}")
else:
    print("No exception occurred.")