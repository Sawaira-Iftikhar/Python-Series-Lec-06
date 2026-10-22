"""
============================================
  LECTURE 6 - FILE 3: RECURSION
  Topics: Base Case, Recursive Case, Call Stack,
          Factorial, Fibonacci, Sum, Power
  Total Questions: 
============================================
"""

# ==========================================
#  PART A: UNDERSTANDING RECURSION 
# ==========================================

# Q1. YOUR FIRST RECURSIVE FUNCTION — Countdown:
#     Define a recursive function countdown(n) that prints numbers
#     from n down to 1, then prints " Blast off!"
#
#     Base case: when n <= 0, print " Blast off!" and return
#     Recursive case: print n, then call countdown(n - 1)
#
#     Call: countdown(5)
#


def countdown(n):
     # Base case
    if n <= 0:
        print(" Blast off!")
        return

    # Recursive case
    print(n)
    countdown(n - 1)

    # Calling the function
countdown(5)

#--------------------------------------------------------------------------------------------

# Q2. RECURSIVE SUM:
#     Define a function recursive_sum(n) that returns the sum of
#     all numbers from 1 to n using recursion.
#
#     Base case: if n == 1, return 1
#     Recursive case: return n + recursive_sum(n - 1)
#
#     Test:
#     recursive_sum(5)  → 15  (1+2+3+4+5)
#     recursive_sum(10) → 55
#     recursive_sum(1)  → 1



def recursive_sum(n):
    # Base case
    if n == 1:
        return 1

   # Recursive case
    return n + recursive_sum(n - 1)

# Testing the function
print("recursive_sum(5) =", recursive_sum(5))
print("recursive_sum(10) =", recursive_sum(10))
print("recursive_sum(1) =", recursive_sum(1))

#     BONUS: Trace the call stack for recursive_sum(4) in a comment:
#     recursive_sum(4)
#     → 4 + recursive_sum(3)
#     → 4 + 3 + recursive_sum(2)
#     → 4 + 3 + 2 + recursive_sum(1)
#     → 4 + 3 + 2 + 1 = 10

#-------------------------------------------------------------------------------------------

# ==========================================
#  PART B: CLASSIC RECURSIVE PROBLEMS 
# ==========================================

# Q3. FACTORIAL:
#     Define a function factorial(n) that returns n!
#     n! = n × (n-1) × (n-2) × ... × 1
#     0! = 1 (base case)



def factorial(n):
    # Check for negative numbers
    if n < 0:
        return "Error: negative number"

    # Base case
    if n == 0:
        return 1

    # Recursive case
    return n * factorial(n - 1)

# Testing the function
print("factorial(0) =", factorial(0))
print("factorial(1) =", factorial(1))
print("factorial(5) =", factorial(5))
print("factorial(10) =", factorial(10))
print("factorial(-2) =", factorial(-2))

#-----------------------------------------------------------------------------------------

# Q4. FIBONACCI SEQUENCE:
#     Define a function fibonacci(n) that returns the nth Fibonacci number.
#     F(0) = 0, F(1) = 1
#     F(n) = F(n-1) + F(n-2)
#
#     Test:
#     fibonacci(0) → 0
#     fibonacci(1) → 1
#     fibonacci(6) → 8
#     fibonacci(10) → 55

def fibonacci(n):
     # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the function
print("fibonacci(0) =", fibonacci(0))
print("fibonacci(1) =", fibonacci(1))
print("fibonacci(6) =", fibonacci(6))
print("fibonacci(10) =", fibonacci(10))

# BONUS: Print the first 10 Fibonacci numbers
numbers = []

for i in range(10):
    numbers.append(fibonacci(i))

print("First 10 Fibonacci:", ", ".join(map(str, numbers)))

#-----------------------------------------------------------------------------------------

# Q5. POWER FUNCTION:
#     Define a function power(base, exp) using recursion.
#     Do NOT use the ** operator or math.pow().
#
#     Base case: if exp == 0, return 1
#     Recursive case: return base * power(base, exp - 1)
#
#     Test:
#     power(2, 10) → 1024
#     power(3, 4)  → 81
#     power(5, 0)  → 1


def power(base, exp): 
        # Base case
    if exp == 0:
        return 1

     # Handle negative exponents
    if exp < 0:
        return 1 / power(base, -exp)

     # Recursive case
    return base * power(base, exp - 1)

# Testing the function
print("power(2, 10) =", power(2, 10))
print("power(3, 4) =", power(3, 4))
print("power(5, 0) =", power(5, 0))

# BONUS: Negative exponent
print("power(2, -3) =", power(2, -3))

#-----------------------------------------------------------------------------------------

# Q6. RECURSIVE STRING REVERSAL:
#     Define a function reverse_string(s) that reverses a string
#     using recursion. Do NOT use slicing [::-1].
#
#     Base case: if len(s) <= 1, return s
#     Recursive case: return reverse_string(s[1:]) + s[0]
#
#     Test:
#     reverse_string("Python") → "nohtyP"
#     reverse_string("Hello")  → "olleH"
#     reverse_string("a")      → "a"



def reverse_string(s):
    # Base case
    if len(s) <= 1:
        return s

     # Recursive case
    return reverse_string(s[1:]) + s[0]

# Testing the function
print('reverse_string("Python") =', reverse_string("Python"))
print('reverse_string("Hello") =', reverse_string("Hello"))
print('reverse_string("a") =', reverse_string("a"))

#     Trace for "Hi":
#     reverse_string("Hi")
#     → reverse_string("i") + "H"
#     → "i" + "H"
#     → "iH"

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART C: ADVANCED RECURSION 
# ==========================================

# Q7. RECURSIVE LIST SUM:
#     Define a function sum_list(lst) that returns the sum of all
#     elements in a list using recursion. Do NOT use sum() or loops.
#
#     Base case: if list is empty, return 0
#     Recursive case: return lst[0] + sum_list(lst[1:])
#
#     Test:
#     sum_list([1, 2, 3, 4, 5]) → 15
#     sum_list([10]) → 10
#     sum_list([]) → 0


def sum_list(lst):
    # Base case
    if len(lst) == 0:
        return 0

    # Recursive case
    return lst[0] + sum_list(lst[1:])

# Testing the function
print("sum_list([1, 2, 3, 4, 5]) =", sum_list([1, 2, 3, 4, 5]))
print("sum_list([10]) =", sum_list([10]))
print("sum_list([]) =", sum_list([]))

#------------------------------------------------------------------------------------------