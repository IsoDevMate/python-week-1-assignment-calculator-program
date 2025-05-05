def calculator():
    # Get user input
    print("Welcome to Basic Calculator!")

    # Get first number
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get second number
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get operation
    print("\nAvailable operations:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")

    while True:
        operation = input("\nEnter operation symbol: ")
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operation. Please use +, -, *, or /.")

    # Perform calculation
    if operation == '+':
        result = num1 + num2
        op_name = "addition"
    elif operation == '-':
        result = num1 - num2
        op_name = "subtraction"
    elif operation == '*':
        result = num1 * num2
        op_name = "multiplication"
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        op_name = "division"

    # Display result
    print(f"\nResult of {op_name}:")
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()
