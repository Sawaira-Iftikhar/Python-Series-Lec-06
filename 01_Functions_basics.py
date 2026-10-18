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
