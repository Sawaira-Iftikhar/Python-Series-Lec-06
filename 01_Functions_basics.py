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

# 4. Call the return function and print its result
result = format_box("Hello")
print(result)

"""
 5.  Difference:
 print_box() displays the output directly and returns None.
 format_box() returns a string that can be stored in a variable
 and printed or used later.
"""
#------------------------------------------------------------------------------------------

# ==========================================
#  PART B: TYPES OF FUNCTIONS 
# ==========================================

# Q5. BUILT-in vs USER-DEFINED FUNCTIONS:
#     a) List 5 built-in functions you've used so far and call each one
#     b) Write a user-defined function is_even(n) that returns True/False
#     c) Write a user-defined function celsius_to_fahrenheit(c)
#        Formula: F = (C × 9/5) + 32
#     d) Test both functions


# 1. Five built-in functions
print('len("Python") =', len("Python"))
print("max(10, 20, 30) =", max(10, 20, 30))
print("min(10, 20, 30) =", min(10, 20, 30))
print("sum([1, 2, 3, 4, 5]) =", sum([1, 2, 3, 4, 5]))
print("type(25) =", type(25))

# 2. User-defined function to check even numbers
def is_even(n):
    return n % 2 == 0

# 3. User-defined function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

# 4. Test both functions
print("is_even(4) =", is_even(4))
print("is_even(7) =", is_even(7))

print("100°C =", celsius_to_fahrenheit(100), "°F")

#-----------------------------------------------------------------------------------------

# Q6. LAMBDA vs def COMPARISON:
#     Rewrite each lambda as a regular def function and vice versa:
#
#     a) Lambda: cube = lambda x: x ** 3
#        → Rewrite as def
#
#     b) def:
#        def absolute(n):
#            return n if n >= 0 else -n
#        → Rewrite as lambda
#
#     c) When should you use lambda vs def? Explain in a comment.



# 1. Lambda to def
def cube(x):
    return x ** 3

# 2. def to lambda
absolute = lambda n: n if n >= 0 else -n

# Testing both functions
print("Cube of 3:", cube(3))
print("Absolute of -7:", absolute(-7))

# 3. When to use lambda vs def?
"""
Use lambda for short, simple, one-line functions.
Use def for longer functions with multiple statements
or when the function needs more explanation and readability.
"""
#-----------------------------------------------------------------------------------------

# ==========================================
#  PART C: FUNCTION BEHAVIOR & SCOPE 
# ==========================================

# Q7. FUNCTION CALLING ANOTHER FUNCTION:
#     a) Define a function square(n) that returns n * n
#     b) Define a function sum_of_squares(a, b) that uses square()
#        to return square(a) + square(b)
#     c) Define a function pythagoras(a, b) that uses sum_of_squares()
#        and returns the square root (use ** 0.5)
#     d) Test: pythagoras(3, 4) should return 5.0
