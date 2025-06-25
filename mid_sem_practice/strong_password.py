print('Create your account \n  Rules: At least 8 characters, \n \t At least 1 digit');
password = input('\n Enter password: ')
count = 1
while count < 5:
  if(len(password) < 8):
    print('The password should have at least 8 characters.')
    password = input(f'{5 - count} attempts left. Try again: ')
    count += 1
  elif(password.isalpha()):
    print('The password should have atleast 1 digit.')
    password = input(f'{5 - count} attempts left. Try again: ')
    count += 1
  else:
    print('Strong password. Account successfully created.')
    break
if count == 5:
  if not password.isalpha() and len(password) >= 8:
    print('Strong password. Account successfully created.')
  else:
    print(f'You have exhausted your {count} attempts. Try again in one hour.')
