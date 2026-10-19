"""
============================================
  LECTURE 6 - FILE 2: DEFAULT PARAMETERS & ADVANCED
  Topics: Default Parameters, Keyword Arguments,
          *args, **kwargs
  Total Questions: 
============================================
"""

# ==========================================
#  PART A: DEFAULT PARAMETERS 
# ==========================================

# Q1. BASIC DEFAULT PARAMETERS:
#     Define a function greet(name, greeting="Hello", punctuation="!")
#     that returns a formatted greeting string.
#
#     Call it in these ways:
#     "Hello, Ali!"
#     "Hi, Sara!"
#     "Hey, Hamza!!!"
#      "Hello, Zainab?"


def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

# Testing the function
print(greet("Ali"))
print(greet("Sara", "Hi"))
print(greet("Hamza", "Hey", "!!!"))
print(greet("Zainab", punctuation="?"))

#-----------------------------------------------------------------------------------------

# Q2. DEFAULT PARAMETERS WITH CALCULATIONS:
#     Define a function calculate_salary(base, bonus=5000, tax_rate=0.1)
#     that returns the net salary after adding bonus and deducting tax.
#     Formula: net = (base + bonus) * (1 - tax_rate)
#
#     Call it:
#     a) calculate_salary(50000)                  → default bonus & tax
#     b) calculate_salary(50000, 10000)           → custom bonus
#     c) calculate_salary(50000, 10000, 0.15)     → custom bonus & tax
#     d) calculate_salary(50000, tax_rate=0.2)    → skip bonus, custom tax


def calculate_salary(base, bonus=5000, tax_rate=0.1):
    net = (base + bonus) * (1 - tax_rate)
    return net

# Testing the function
print("Net Salary (default):", calculate_salary(50000))
print("Net Salary (bonus 10k):", calculate_salary(50000, 10000))
print("Net Salary (15% tax):", calculate_salary(50000, 10000, 0.15))
print("Net Salary (20% tax):", calculate_salary(50000, tax_rate=0.2))

#-----------------------------------------------------------------------------------------