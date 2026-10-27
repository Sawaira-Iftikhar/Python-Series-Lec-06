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

    else:
        return "Error: Unknown operation"

     # Round the result to the specified precision
    return round(result, precision)

# 2. Lambda function to format the result
format_result = lambda number: f"Result: ${number:.2f}"

# 4. Test the calculator
print("=" * 50)
print("            SMART CALCULATOR")
print("=" * 50)

# Addition
result = calculate("add", 10, 20, 30)
print("add(10, 20, 30):")
print(f"  Raw: {result} | Formatted: {format_result(result)}")
print()

# Average
result = calculate("average", 85, 92, 78, 95, precision=1)
print("average(85, 92, 78, 95, precision=1):")
print(f"  Raw: {result} | Formatted: {format_result(result)}")
print()

# Multiplication
result = calculate("multiply", 2, 3, 4, 5)
print("multiply(2, 3, 4, 5):")
print(f"  Raw: {result} | Formatted: {format_result(result)}")
print()

# Unknown operation
print("unknown(1, 2):")
print(" ", calculate("unknown", 1, 2))
print()

# No arguments
print("add() [no args]:")
print(" ", calculate("add"))
print("=" * 50)

#------------------------------------------------------------------------------------------

# ==========================================
#  CHALLENGE 2: The Recursive File System Explorer 
#  Topics: Recursion, Nested Dicts, Default Params, **kwargs
# ==========================================

"""
Simulate a file system explorer using recursion and nested dictionaries.


Tasks:
1. Write a RECURSIVE function display_tree(node, indent=0) that
   prints the file system as a tree structure.
   - Folders get a 📁 icon
   - Files get a 📄 icon with their size
   - Use indent to show nesting depth

2. Write a RECURSIVE function total_size(node) that calculates
   the total size of ALL files in the entire file system.

3. Write a RECURSIVE function find_files(node, extension) that
   returns a list of all file names matching a given extension.
   Example: find_files(file_system, ".py") → ["app.py"]

4. Write a function search_file(node, filename, path="") that
   returns the full path to a file.
   Example: search_file(file_system, "data.csv") → "root/Documents/Projects/data.csv"
"""

# Given File System Structure:
file_system = {
    "name": "root",
    "type": "folder",
    "children": [
        {
            "name": "Documents",
            "type": "folder",
            "children": [
                {"name": "resume.pdf", "type": "file", "size": 250},
                {"name": "notes.txt", "type": "file", "size": 15},
                {
                    "name": "Projects",
                    "type": "folder",
                    "children": [
                        {"name": "app.py", "type": "file", "size": 45},
                        {"name": "data.csv", "type": "file", "size": 1200}
                    ]
                }
            ]
        },
        {
            "name": "Photos",
            "type": "folder",
            "children": [
                {"name": "vacation.jpg", "type": "file", "size": 3500},
                {"name": "profile.png", "type": "file", "size": 800}
            ]
        },
        {"name": "readme.md", "type": "file", "size": 10}
    ]
}

# 1. Recursive function to display the file system tree
def display_tree(node, indent=0):
     if node["type"] == "folder":
        print("  " * indent + f"📁 {node['name']}")

        for child in node.get("children", []):
            display_tree(child, indent + 1)

     else:
        print("  " * indent + f"📄 {node['name']} ({node['size']} KB)")

# 2. Recursive function to calculate the total size
def total_size(node):
    if node["type"] == "file":
        return node["size"]

    size = 0

    for child in node.get("children", []):
        size += total_size(child)

    return size

# 3. Recursive function to find files by extension
def find_files(node, extension):
    files = []

    if node["type"] == "file":
        if node["name"].endswith(extension):
            files.append(node["name"])

    else:
        for child in node.get("children", []):
            files.extend(find_files(child, extension))

    return files

# 4. Function to search for a file and return its full path
def search_file(node, filename, path=""):
    current_path = f"{path}/{node['name']}" if path else node["name"]

    if node["type"] == "file":
        if node["name"] == filename:
            return current_path
        return None

    for child in node.get("children", []):
        result = search_file(child, filename, current_path)

        if result is not None:
            return result

    return None

# Display results
print("=" * 50)
print("        📁 FILE SYSTEM EXPLORER")
print("=" * 50)

display_tree(file_system)

print("-" * 50)
print("Total Size:", total_size(file_system), "KB")
print("Python Files:", find_files(file_system, ".py"))
print("Path to data.csv:", search_file(file_system, "data.csv"))

print("=" * 50)

#-------------------------------------------------------------------------------------------

# ==========================================
#  CHALLENGE 3: The Tower of Hanoi Solver
#  Topics: Recursion, Default Params, Function Composition
# ==========================================

"""
Solve the classic Tower of Hanoi puzzle using recursion.

Rules:
- You have 3 rods: Source (A), Auxiliary (B), Destination (C)
- Move n disks from A to C using B as helper
- Only one disk can be moved at a time
- A larger disk can NEVER be placed on top of a smaller disk

Tasks:
1. Write a RECURSIVE function hanoi(n, source="A", aux="B", dest="C")
   that prints each move step by step.

2. Write a function count_moves(n) that returns the total number
   of moves required for n disks. (Formula: 2^n - 1, but implement
   it recursively!)

3. Write a wrapper function solve_hanoi(n) that:
   - Validates n (must be positive integer)
   - Prints the total moves needed
   - Calls hanoi() to show all steps
   - Uses a default parameter for showing/hiding steps

4. Test with n = 3 and n = 4.

"""

"""
                         TOWER OF HANOI
"""

# 1. Recursive function to solve Tower of Hanoi
def hanoi(n, source="A", aux="B", dest="C", step=[0]):

    # Base case: Only one disk needs to be moved
    if n == 1:
        step[0] += 1
        print(f"Step {step[0]}: Move disk 1 from {source} → {dest}")
        return

    # Move n-1 disks from source to auxiliary
    hanoi(n - 1, source, dest, aux, step)

     # Move the largest disk from source to destination
    step[0] += 1
    print(f"Step {step[0]}: Move disk {n} from {source} → {dest}")


     # Move n-1 disks from auxiliary to destination
    hanoi(n - 1, aux, source, dest, step)

# 2. Recursive function to count total moves
def count_moves(n):

    # Base case
    if n == 0:
        return 0

    # Recursive case: 2 * moves for n-1 disks + 1 move
    return 2 * count_moves(n - 1) + 1

# 3. Wrapper function to solve the puzzle
def solve_hanoi(n, show_steps=True):

     # Validate input
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        print("Error: Number of disks must be a positive integer.")
        return

    print("=" * 50)
    print("           TOWER OF HANOI")
    print("=" * 50)

    print(f"Solving for {n} disks...")

    total = count_moves(n)
    print(f"Total moves required: {total}")

    if show_steps:
        print("-" * 50)