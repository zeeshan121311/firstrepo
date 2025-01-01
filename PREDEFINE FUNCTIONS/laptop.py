laptop = ["hp", "dell", "asus", "lenavo", "apple"]
mobile = ["samsung", "oppo", "techno", "redmi", "realme"]

items = input("Enter the names of laptops or mobiles (separate by spaces or commas): ")

item_list = items.replace(",", " ").split()

for name_yz in item_list:
    if name_yz == 'exit':
        print("Encountered 'exit' - Exiting the program.")
        break
    elif name_yz in laptop:
        print(f"{name_yz} is a laptop.")
    elif name_yz in mobile:
        print(f"{name_yz} is a mobile.")
    else:
        print(f"{name_yz} is not recognized.")
