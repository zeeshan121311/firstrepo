# Function to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return f"{num} is positive."
    elif num < 0:
        return f"{num} is negative."
    else:
        return f"{num} is zero."

# Input from the user
number = int(input("Enter a number: "))

# Check the number
result = check_number(number)

# Display the result
print(result)