scores = '87, 65, 88, 53, 42, 91, 77, and 66'
grades = {'A':0,'B':0, 'C':0, 'D':0, 'F':0}
scores = scores.replace('and ', '').split(', ')
for score in scores:
 score = int(score)
 if score >= 90:
  grades['A'] += 1
 elif score >= 80: 
  grades['B'] += 1
 elif score >= 70: 
  grades['C'] += 1
 elif score >= 60: 
  grades['D'] += 1
 else:
  grades['F'] += 1
for grade in grades:
 print(f'Grade {grade} holds {grades[grade]} students \n')