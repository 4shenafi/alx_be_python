def perform_operation(num1: float, num2: float, operations: str):
    match operations:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                print("Division by zero not possible!")
            else:
                return num1 / num2