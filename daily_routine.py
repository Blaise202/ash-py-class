daily_routine = 'Wake up, shower, eat breakfast, attend class,return home, eat dinner, go to bed.'
array = daily_routine.split(',')
count = 1
for i in array:
    print(f'{count}. {i.strip()}')
    count += 1