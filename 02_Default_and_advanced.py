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

# 1. All positional arguments
print(book_flight("Lahore", "Karachi", "2025-01-15"))

# 2. All keyword arguments (in any order)
print(book_flight(to_city="Lahore", date="2025-02-20",
                  seat="Business", from_city="Karachi"))

# 3. Mixed positional and keyword arguments
print(book_flight("Lahore", "Islamabad",
                  date="2025-03-10", seat="Business"))

# 4. Keyword argument before a positional argument
# print(book_flight(from_city="Lahore", "Karachi", "2025-01-15"))
# SyntaxError: positional argument follows keyword argument

#-----------------------------------------------------------------------------------------

#  Q5. KEYWORD-ONLY ARGUMENTS (using *):
#     Define a function send_email(to, subject, *, cc=None, bcc=None, urgent=False)
#     The * forces cc, bcc, and urgent to be keyword-only.
#
#     a) Call it correctly with keyword args for cc and urgent
#     b) Try calling it with cc as a positional arg → Write the error


def send_email(to, subject, *, cc=None, bcc=None, urgent=False):
      print(f"Sending email to {to}")
      print(f"Subject: {subject}")
      print(f"CC: {cc} | Urgent: {urgent}")


# 1. Correct call using keyword arguments
send_email(
    "ali@test.com",
    "Meeting Tomorrow",
    cc="sara@test.com",
    urgent=True
)

# 2. Incorrect call: cc passed as a positional argument
# send_email("ali@test.com", "Meeting Tomorrow", "sara@test.com")
# TypeError: send_email() takes 2 positional arguments but 3 were given

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART C: *args & **kwargs 
# ==========================================

# Q6. *args — VARIABLE POSITIONAL ARGUMENTS:
#     a) Define a function total_sum(*args) that returns the sum of
#        all arguments passed to it.
#     b) Call it with: total_sum(1, 2, 3)
#     c) Call it with: total_sum(10, 20, 30, 40, 50)
#     d) Call it with: total_sum() (no arguments — should return 0)
#     e) What is the TYPE of *args inside the function? Print it.


# 1. Function to calculate the sum of all arguments
def total_sum(*args):
    print("Type of args:", type(args))
    return sum(args)

# 2. Call with three arguments
print("total_sum(1, 2, 3) =", total_sum(1, 2, 3))

# 3. Call with five arguments
print("total_sum(10, 20, 30, 40, 50) =", total_sum(10, 20, 30, 40, 50))

# 4. Call with no arguments
print("total_sum() =", total_sum())

#---------------------------------------------------------------------------------------

# Q7. **kwargs — VARIABLE KEYWORD ARGUMENTS:
#     a) Define a function print_info(**kwargs) that prints each
#        key-value pair on a new line.
#     b) Call it with: print_info(name="Ali", age=22, city="Lahore")
#     c) What is the TYPE of **kwargs inside the function? Print it.



# 1. Function to print each key-value pair
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    print("Type of kwargs:", type(kwargs))

# 2. Call the function
print_info(name="Ali", age=22, city="Lahore")

#-----------------------------------------------------------------------------------------

# Q8. COMBINING *args AND **kwargs:
#     Define a function create_order(customer_name, *items, **details)
#     that prints an order summary.
#
#     Call it:
#     create_order("Ali", "Laptop", "Mouse", "Keyboard",
#                  payment="Credit Card", delivery="Express")


def create_order(customer_name, *items, **details):
    print("==============================")
    print(f"Order for: {customer_name}")

    print("Items:")
    for index, item in enumerate(items, start=1):
        print(f"  {index}. {item}")

    print("Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

    print("==============================")

# Calling the function
create_order(
    "Ali",
    "Laptop",
    "Mouse",
    "Keyboard",
    payment="Credit Card",
    delivery="Express"
)

#-----------------------------------------------------------------------------------------

# Q9. UNPACKING WITH * AND **:
#      Given:
#      numbers = [1, 2, 3, 4, 5]
#      config = {"theme": "dark", "lang": "en", "font_size": 14}
#
#      a) Define a function show_numbers(a, b, c, d, e) and call it
#         by unpacking the list: show_numbers(*numbers)
#      b) Define a function show_config(theme, lang, font_size) and call it
#         by unpacking the dict: show_config(**config)
#      c) What happens if the list/dict size doesn't match the parameters?


numbers = [1, 2, 3, 4, 5]
config = {"theme": "dark", "lang": "en", "font_size": 14}

# 1. Unpacking a list using *
def show_numbers(a, b, c, d, e):
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}")

show_numbers(*numbers)

# 2. Unpacking a dictionary using **
def show_config(theme, lang, font_size):
    print(f"theme={theme}, lang={lang}, font_size={font_size}")