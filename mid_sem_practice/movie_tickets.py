number = input('How many tickets are we selling: ')
correct = False
skipped = 0
while not correct:
  if '.' in number or not float(number) or float(number) < 0:
    number = input('The number should be a positive integer. Try again: ')
  else:
    number = float(number)
    number = int(number)
    correct = True
for i in range(number):
  choice = input('Do you want to sell a ticket? [Y or yes/ N or No]: ')
  if choice in ['Y', 'yes']:
    print(f'Ticket sold. {number - i + 1} to go.')
    i += 1
  elif choice in ['N', 'no']:
    print(f'Ticket Skiped. {number - i + 1} to go.')
    skipped += 1
    i += 1
  else:
    print('Invalid input')
print(f'Tickets are finished. We sold {number - skipped} and skipped {'none' if skipped == 0 else skipped }')
