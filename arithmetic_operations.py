def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1: First number as float
        num2: Second number as float
        operation: String specifying operation ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        Result of the operation as float, or error message for division by zero,
        or None for invalid operations
    
    Examples:
        >>> perform_operation(5, 3, 'add')
        8.0
        >>> perform_operation(5, 0, 'divide')
        'Error: Division by zero'
    """
    # Convert operation to lowercase to make it case-insensitive
    operation = operation.lower()
    
    # Perform the requested operation
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"  # Special handling for division by zero
        return num1 / num2
    else:
        return None  # Return None for invalid operation names