# Calculator function
    
while True:
    print("Choose an option:")
    print("1. Perform Calculation")  
    print("2. Exit")
        
    choice = input("Enter 1 or 2: ")
        
    if choice == '1':  
         num1 = float(input("Enter the first number: "))
         operation = input("Choose an operation (+, -, *, /): ") 
         num2 = float(input("Enter the second number: "))
       
    elif choice == '2': 
          print("Closing the calculator. Thank you!")
          break
    if operation == '+':
        print(num1 + num2)  
    elif operation == '-':
        print(num1 + num2)
    elif operation == '*':
        print(num1 + num2)
    elif operation == '/':
        if num2 != 0:  
            print(num1 + num2)
        else:
            print(" Division by zero is not allowed.")
    else:
        print("Invalid option! Please enter 1 to calculate or 2 to exit."
              "Invalid operation! Please use +, -, *, or /.")