age = int(input("Enter your age: "))
if age >= 18:
    print("You can both vote and drive.")
elif age >= 16:
    print("You can only drive.")
else:
    print("You can neither vote nor drive.")
    