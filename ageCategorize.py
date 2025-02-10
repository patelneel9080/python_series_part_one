age = int(input("Enter age : "))

if age >= 0 and age <= 12 :
    print("Child (0-12)")
elif age >= 13 and age <= 19:
    print("Teenager (13-19)")
elif age >= 20 and age <= 59:
    print("Adult (20-59)")
elif age >= 60:
    print("Senior (60+)")
else:
    print("Invalid age")
