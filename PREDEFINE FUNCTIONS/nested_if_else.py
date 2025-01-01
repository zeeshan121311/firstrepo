
ticket_price = get_ticket_price(age, is_student):
    if age < 0:
        print ("Invalid age")
    elif age <= 12:
        print("5") 
    elif age <= 17:
        price = 7
    elif age <= 64:
        price = 12
    else:
        print ("6")

    if is_student and 13 <= age <= 64:
        price -= 2
    
    print ("price")

age = int(input("Enter your age: "))
ticket_price = get_ticket_price(age, is_student)

print(f"The ticket price is: ${ticket_price}")