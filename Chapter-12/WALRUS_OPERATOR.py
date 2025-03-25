"""
The walrus operator (:=), introduced in Python 3.8, allows you to assign values to 
variables as part of an expression. This operator, named for its resemblance to the eyes 
and tusks of a walrus, is officially called the "assignment expression." 
"""


# The walrus operator can be particularly useful in situations where you want to both
# assign a value to a variable and use that value in a condition or expression.
# This can help reduce redundancy and make your code more concise.
# For example, instead of writing:
#
# x = some_function()
# if x > 10:
#     print(x)
# You can use the walrus operator to combine these two lines into one:
# if (x := some_function()) > 10:
#     print(x)
# This way, you avoid calling some_function() twice and make your code cleaner.

# Example 1: Using the walrus operator in an if statement
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") 
 
# Output: List is too long (5 elements, expected <= 3)

# Example 2: Using the walrus operator in a while loop
count = 0
while (count := count + 1) < 5:
    print(count)
# Output: 1, 2, 3, 4
# The walrus operator allows you to assign the value of count in the while loop condition,

# Example 3: Using the walrus operator in a list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [y := x**2 for x in numbers if y > 5]
print(squared_numbers)  # Output: [9, 16, 25]