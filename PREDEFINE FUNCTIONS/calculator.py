num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = input("Enter choice (1/2/3/4): ")

# Perform the calculation based on the chosen operation
if operation == '1': 
    print("Result:", num1 + num2)
elif operation == '2':
    print("Result:", num1 - num2)
elif operation == '3':
    print("Result:", num1 * num2)
elif operation == '4':
    print("Result:", num1 / num2 if num2 != 0 else "Cannot divide by zero")
else:
    print("Invalid input")