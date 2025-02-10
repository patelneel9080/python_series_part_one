# Implement a program that:
# - Takes three integers as input.
# - Uses an if-elif-else statement to find and print the largest number.

firstNo = int(input("Enter firstNo : "))
secondNo = int(input("Enter secondNo : "))
thirdNo = int(input("Enter thirdNo : "))

if firstNo == secondNo and secondNo == thirdNo:
    print("All numbers are same")
elif firstNo == secondNo:
    print("First number and second number are same")
elif firstNo == thirdNo:
    print("First number and third number are same")
elif secondNo == thirdNo:
    print("Second number and third number are same")
else:
    if firstNo > secondNo:
        if firstNo > thirdNo:
            print("" + str(firstNo) , "is largest number")
        else:
            print("" + str(thirdNo) , "is largest number")
    else:
        if secondNo > thirdNo:
            print("" + str(secondNo) , "is largest number")
        else:
            print("" + str(thirdNo) , "is largest number")
