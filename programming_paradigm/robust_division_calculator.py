def safe_divide(numerator, denominator):
    """
    Performs division and handles errors:
    - Division by zero
    - Non-numeric input
    Returns result or appropriate error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
