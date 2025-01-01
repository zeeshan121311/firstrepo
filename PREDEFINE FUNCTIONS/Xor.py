price = []
ageGroup = []
dict_list = {}


company = int(input("How Many Age Group Would You Like To Add: "))
count = 0
if company <= 4:
     while count < company:
         ageGroup.append(input(f"{count} AgeGroup: "))
         price.append(int(input(f"{count} Price: ")))
         dict_list.update({ageGroup[count]:price[count]})
         count = count + 1
else:
     print("We Can Add Only Upto 4.")

print(dict_list)
