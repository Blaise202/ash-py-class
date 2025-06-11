i = 1
right =0;
print('write the text "Practice makes perfect" 5 times')
while i<=5:
  text = input(f'{i}:')
  if text == 'Practice makes perfect':
    right += 1
  i += 1
print(f'You wrote the text correctly {right} time(s).')
