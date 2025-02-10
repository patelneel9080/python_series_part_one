# Write a Python program using a switch-case equivalent to:
# - Take an operator ('+',,,) as input.
# - Perform the corresponding operation on two numbers entered by the user.\

while True:
   
   
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 5 for exit")
    
    a = int(input("Enter your choice : "))
    
    firstNo = int(input("Enter first number : "))
    secondNo = int(input("Enter second number : "))
    
    
    
    if a == 1:
        print(firstNo + secondNo)
    elif a == 2:
        print(firstNo-secondNo)
    elif a == 3:
        print(firstNo*secondNo)
    elif a == 4:
        print(firstNo/secondNo)
    elif a == 5:
        break
    else:
        print("Invalid choice")
        
    print("\n")
