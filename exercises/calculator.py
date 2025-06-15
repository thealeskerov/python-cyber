# Simple calculator that adds, subtracts, multiplies or divides two numbers

# Ask user for first number
num1 = float(input("Enter first number: "))

# Ask for operation
operator = input("Enter operator (+, -, *, /): ")

# Ask for second number
num2 = float(input("Enter second number: "))

# Check which operation user selected
if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero!")  # Prevent division by 0
else:
    print("Invalid operator")  # User typed something wrong
