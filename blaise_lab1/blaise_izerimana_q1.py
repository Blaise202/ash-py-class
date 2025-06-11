balance = 100
status = True
print('select the event');
while status:
    print('1:New Deposit \t\t 2:Withdrawal \t\t 3:Record Interest \t\t 4:Monthly Fee \t\t 5: Exit')
    choice = input()
    if choice == '1':
       amount = float(input('How much is the new deposit: '))
       balance += amount
    elif choice == '2':
        amount = float(input('How much did you withdraw: '))
        balance -= amount
    elif choice == '3':
        balance -= balance*5/100
    elif choice == '4':
        balance -= 10
    elif choice == '5':
        print('The program closed')
        status = False
    else:
        print('Invalid input')
    print('The current balance is: ', balance)