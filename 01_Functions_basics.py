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

def min_max(numbers):
    return min(numbers), max(numbers)

# Call the function
result = min_max([45, 12, 89, 33, 67])

# Unpack the returned tuple
lowest, highest = result

# Print both values
print("Minimum:", lowest)
print("Maximum:", highest)

#-----------------------------------------------------------------------------------------

# Q4. VOID vs RETURN FUNCTIONS:
#     a) Define a VOID function print_box(message) that prints:
#        ==========
#        | message |
#        ==========
#     b) Define a RETURN function format_box(message) that RETURNS
#        the same formatted string instead of printing it.
#     c) Call print_box("Hello") — it prints directly
#     d) Call format_box("Hello") — store result and print it
#     e) Explain the difference in a comment



# 1. Void function: prints the formatted box directly
def print_box(message):
    print("==========")
    print(f"| {message} |")
    print("==========")

# 2. Return function: returns the formatted box as a string
def format_box(message):
    return f"==========\n| {message} |\n=========="

# 3. Call the void function
print_box("Hello")