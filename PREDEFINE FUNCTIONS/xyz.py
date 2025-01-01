age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    ticket_price = 5  # Children price
elif age <= 17:
    ticket_price = 7  # Teenagers price
elif age <= 64:
    ticket_price = 12  # Adults price
else:
    ticket_price = 6  # Seniors price
    
print("The ticket price is: ${ticket_price}")