count = input('Enter the number of students we are registering: ')
correct = False
while not correct:
    try:
        count= float(count)
        if count%1 != 0 or int(count) < 0:
            count = input('Only positive integer number is allowed. Try again: ')
        else:
            count = int(count)
            correct = True
    except ValueError:
        count = input('Only positive integer number is allowed. Try again: ')

for student in range(1,count+1):
    print(f"Student {student} info:")
    name = ''
    correct_id = False
    while len(name) < 3 or not correct_id:
        name = input('Provide the student full name: ')
        try:
            studentId = int(input("Provide student Id (8-Digits ONLY): "))
            correct_id = True
        except ValueError:
            correct_id = False
        if len(name) >= 3 and correct_id:
            break
        else:
            print('Name must be atleast 3 characters and id must be an 8 integer number. Please try again.')
    has_tuition = input(f'Does {name} have full tuition? "yes" or "no": ')
    invalid_choice = True
    while invalid_choice:
        if has_tuition == 'yes':
            tuition = True
            break
        elif has_tuition == 'no':
            tuition = False
            break
        else:
            print("Invalid Input try again")
            has_tuition = input(f'Does {name} have full tuition? "yes" or "no": ')
        
    if tuition:
        count = input('How many courses passed: ')
        correct = False
        while not correct:
            try:
                count= float(count)
                if count%1 != 0 or int(count) < 1 or int(count) > 5:
                    count = input('Only positive integer number between 1-5 is allowed. Try again: ')
                else:
                    count = int(count)
                    correct = True
            except ValueError:
                count = input('Only positive integer number between 1-5 is allowed. Try again: ')
          
