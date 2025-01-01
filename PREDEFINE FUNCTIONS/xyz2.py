age_price_dict = {}

variable = int(input("How Many Age Groups Would You Like To Add: "))
count = 1

if variable <= 4:
    while count <= variable:
        age_group = input(f"{count} Age Group: ")
        price = int(input(f"{count} Price: "))
        age_price_dict[age_group] = price
        count += 1
else:
    print("We Can Add Only Up To 4.")

print(age_price_dict)
