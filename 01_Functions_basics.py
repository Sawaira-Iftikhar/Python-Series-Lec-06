"""
============================================
  LECTURE 6 - FILE 1: FUNCTIONS BASICS & TYPES
  Topics: def, return, Parameters, Arguments,
          Types of Functions (Built-in, User-defined,
          Lambda, Void)
  Total Questions: 
============================================
"""

# ==========================================
#  PART A: CREATING & CALLING FUNCTIONS 
# ==========================================

# Q1. YOUR FIRST FUNCTION:
#     a) Define a function called greet() that prints "Hello, World!"
#     b) Call the function 3 times
#     c) What does greet() return if there is no return statement?
#        Store the result in a variable and print it.

def greet():
    print("Hello, World!")

# Call the function 3 times
greet()
greet()
greet()

# Store and print the return value
result = greet()
print("Return value:", result)

#-----------------------------------------------------------------------------------------

# Q2. FUNCTIONS WITH PARAMETERS:
#     a) Define a function add(a, b) that returns the sum of two numbers
#     b) Define a function multiply(a, b) that returns the product
#     c) Define a function power(base, exp) that returns base ** exp
#     d) Call each function and print the results

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def power(base, exp):
    return base ** exp

# Call each function and print the results
print("add(5, 3) =", add(5, 3))
print("multiply(4, 7) =", multiply(4, 7))
print("power(2, 10) =", power(2, 10))

#-----------------------------------------------------------------------------------------

# Q3. FUNCTIONS WITH MULTIPLE RETURNS:
#     Define a function min_max(numbers) that takes a list of numbers
#     and returns BOTH the minimum and maximum values as a tuple.
#
#     a) Call it with [45, 12, 89, 33, 67]
#     b) Unpack the returned tuple into two variables: lowest, highest
#     c) Print both values
