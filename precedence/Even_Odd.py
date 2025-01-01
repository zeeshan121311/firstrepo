number = int(input("Enter a number: "))
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even."
    else:
        return f"{num} is Odd."
# Check if the number is even or odd
result = check_even_odd(number)
print(result)