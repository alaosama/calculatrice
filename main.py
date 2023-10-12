while True:
    while True:
        try:
            first_number = float(input("X = "))
            break
        except ValueError:
            print("Invalid input. Please enter a number")
    
    while True:   
        try:
            operation = input("Enter operation type: ")
            if operation in ("/", "-", "+", "*"):
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid operator, please enter +,-,/;*")
    
    while True:
        try:
            second_number = float(input("Y = "))
            if second_number == 0 and operation == "/":
                raise ZeroDivisionError
            break
        except ValueError:
            print("Invalid operator, please enter a numeric value")
        except ZeroDivisionError:
            print("Cannot divide by zero, please enter numeric value")
    

    if operation == "+":
        print(first_number + second_number)
    elif operation == "-":
        print(first_number - second_number)
    elif operation == "/":
        print(first_number / second_number)
    elif operation == "*":
        print(first_number * second_number)
    else:
        result = None
        
    if result != None:
        print("Result is:", result)
    else:
        print("unexpected error")
            
            
            
            
            
        
