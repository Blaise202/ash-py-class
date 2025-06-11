right = 0;
print('write the text "Practice makes perfect" 5 times')
for i in range(5):
  text = input(f'{i+1}:')
  if text == 'Practice makes perfect':
    right += 1
print(f'You wrote the text correctly {right} time(s).')
