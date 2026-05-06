# VIOLATION 1: No type hints provided (Medium Severity)
def add_numbers(a, b):
    # VIOLATION 2: Using print() inside the logic (Low Severity)
    print(f"I am adding {a} and {b} right now")
    return a + b

# VIOLATION 1: No type hints provided (Medium Severity)
def calculate_string(math_expression):
    # VIOLATION 3: Using the dangerous eval() function (High Severity)
    result = eval(math_expression)
    return result