# Simple calculator program

# Ask user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user to choose an operation
operation = input("Enter the operation (+, -, *, /, **, %): ")

# Perform the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero."
elif operation == '**':
    result = num1 ** num2
elif operation == '%':
    result = num1 % num2
else:
    result = "Invalid operation."

# Print the result
print("Result:", result)

