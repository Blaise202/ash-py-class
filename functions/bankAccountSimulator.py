def deposit(amount, balance):
  return  balance + amount

def withdraw(amount, balance):
  if balance < amount:
    return 'Insufficient'
  return balance - amount

def interest(amount):
  deduction = amount*5/100
  return amount - deduction

def monthlyDeduction(amount):
  return amount - 100

def validateInput(amount):
  while True:
    try:
      amount = float(amount)
      break
    except ValueError:
      return 'invalid'
  return amount

if __name__ == "__main__":
  balance = 1000
  print("Welcome to your bank account")
  while True:
    choice = input('Please select the action: [1] Deposit, [2] Withdraw, [3] 5% Interest, [4] Monthly Fee, [] Quite:  ')
    if choice == '1':
      while True:
        amount = validateInput(input('How much is the deposite: '))
        if amount != "invalid":
          break
      balance  = deposit(amount, balance)
      print(f'Now the balance is Ghs {balance}')
    elif choice == '2':
      while True:
        amount = validateInput(input('How much is the deposite: '))
        if amount != "invalid":
          break
      new  = withdraw(amount, balance)
      if new == 'Insufficient':
        print(f'Insufficient amount. only {balance} can be withdrawn')
      else:
        print(f'Now the balance is Ghs {new}')
    elif choice == '3':
      while True:
        try: 
          amount = float(input('How much is the withdrawal: '))
          break
        except ValueError:
          print('Invalid input try again')
      new  = withdraw(amount, balance)
      if new == 'Insufficient':
        print(f'Insufficient amount. only {balance} can be withdrawn')
      else:
        print(f'Now the balance is Ghs {new}')