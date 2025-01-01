# Function to compare two numbers
def compare_numbers(num1, num2):
    if num1 > num2:
        return f"{num1} is greater than {num2}."
    elif num1 < num2:
        return f"{num1} is smaller than {num2}."
    else:
        return f"{num1} is equal to {num2}."

# Input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Compare the numbers
result = compare_numbers(number1, number2)

# Display the result
print(result)