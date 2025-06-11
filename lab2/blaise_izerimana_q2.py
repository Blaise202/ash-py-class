number = int(input("Enter a number: "))
if number == 0:
    print("The number is zero.")
if number % 2 == 0:
    if number < 0:
        print("The number is even and not  positive.")
    else:
        print("The number is even and positive.")
else:
    if number < 0:
        print("The number is odd and not  positive.")
    else:
        print("The number is odd and positive.")
