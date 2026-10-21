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

# Q3. DEFAULT PARAMETERS WITH TYPES:
#     Define a function create_profile(name, age, hobbies=None, is_active=True)
#     that returns a dictionary representing a user profile.
#     If hobbies is None, set it to an empty list.
#
#     Call it:
#     a) create_profile("Ali", 22)
#     b) create_profile("Sara", 25, ["Reading", "Coding"])
#     c) create_profile("Hamza", 20, is_active=False)

def create_profile(name, age, hobbies=None, is_active=True):
    if hobbies is None:
        hobbies = []

    return {
        "name": name,
        "age": age,
        "hobbies": hobbies,
        "is_active": is_active
    }

# Testing the function
print(create_profile("Ali", 22))
print(create_profile("Sara", 25, ["Reading", "Coding"]))
print(create_profile("Hamza", 20, is_active=False))

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART B: KEYWORD ARGUMENTS 
# ==========================================

# Q4. POSITIONAL vs KEYWORD ARGUMENTS:
#     Define a function book_flight(from_city, to_city, date, seat="Economy")
#
#     Call it using:
#     a) All positional arguments
#     b) All keyword arguments (in any order!)
#     c) Mixed: positional for from/to, keyword for date and seat
#     d) What happens if you put a keyword arg BEFORE a positional arg?
#        Try: book_flight(from_city="Lahore", "Karachi", "2025-01-15")
#        Write the error as a comment.

def book_flight(from_city, to_city, date, seat="Economy"):
    return f"Flight: {from_city} → {to_city} on {date} ({seat})"