#!/usr/bin/python3
# Import the add function from add_0.py
from add_0 import add

# Assign the value 1 to a variable called a
a = 1

# Assign the value 2 to a variable called b
b = 2

# Print the result of the addition using string format
print("{} + {} = {}".format(a, b, add(a, b)))
