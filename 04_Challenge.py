"""
============================================
  LECTURE 6 - FILE 4: BOSS CHALLENGE 
  Topics: ALL Function Topics Combined
  Total Challenges: 
============================================
"""

# ==========================================
#  CHALLENGE 1: The Smart Calculator Engine 
#  Topics: Functions, Default Params, *args, Lambda, Nested Functions
#  Difficulty: Medium-Hard
# ==========================================

"""
Build a flexible calculator system using multiple function types.

Requirements:
1. Define a function calculate(operation, *args, precision=2) that:
   - Takes an operation name as a string
   - Takes any number of numeric arguments via *args
   - Has a default precision of 2 decimal places
   - Supports these operations:
     * "add"      → sum of all args
     * "multiply" → product of all args
     * "average"  → average of all args
     * "max"      → maximum of all args
     * "min"      → minimum of all args
   - Returns the result rounded to `precision` decimal places
   - If operation is invalid, return "Error: Unknown operation"
   - If no args provided, return "Error: No numbers given"

2. Define a lambda function `format_result` that takes a number
   and returns it formatted as: "Result: $XX.XX"

3. Define a nested function inside calculate called `validate`
   that checks if all args are numbers (int or float).

4. Test with various calls:
   calculate("add", 10, 20, 30)
   calculate("average", 85, 92, 78, 95, precision=1)
   calculate("multiply", 2, 3, 4, 5)
   calculate("unknown", 1, 2)
   calculate("add")
"""


"""
                             SMART CALCULATOR
"""

# 1. Define the calculator function
def calculate(operation, *args, precision=2):

      # 3. Nested function to validate arguments
    def validate():
        return all(isinstance(num, (int, float)) for num in args)

     # Check if arguments are provided
    if not args:
        return "Error: No numbers given"

     # Validate that all arguments are numbers
    if not validate():
        return "Error: All arguments must be numbers"

    # Perform the requested operation
    if operation == "add":
        result = sum(args)

    elif operation == "multiply":
            result = 1
            for num in args:
                result *= num

    elif operation == "average":
        result = sum(args) / len(args)

    elif operation == "max":
        result = max(args)

    elif operation == "min":
        result = min(args)