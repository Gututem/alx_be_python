def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation.

    operation: "add", "subtract", "multiply", or "divide"
    Returns numeric results for valid operations, or one of these exact strings:
      - "Cannot divide by zero."
      - "Invalid operation."
    """
    # Normalize operation input so "Add", " ADD " etc. still work
    if not isinstance(operation, str):
        return "Invalid operation."
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
    else:
        return "Invalid operation."
