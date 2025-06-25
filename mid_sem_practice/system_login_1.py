password = input('Enter the password: ')
i = 0;
for i in range(2):
  if password != 'python123':
   print(f'Incorrect Password.{2-i} attempts remaining remaining')
   password = input('Try again: ')
  else:
   print('Access Granted')
   break
  i += 1
if i == 2:
 if password == 'python123':
  print('Access Granted')
 else:
  print('Access Denied')