def perform_operation(num1: float, num2: float, operation: str):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
        if num2 == 0:
            print("Cannot divide by 0")
            
    return result