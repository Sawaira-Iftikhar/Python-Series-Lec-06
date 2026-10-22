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