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