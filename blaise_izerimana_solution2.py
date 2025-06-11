print('enter name and age')
name = input('Name: ')
age = int(input('Age: '))
if len(name) <= 3:
    print('The name is too short')
elif not name[0].isalpha():
    print('Only proper names are allowed')
if age < 0:
    print('Age cannot be negative')
else:
    if age < 10:
        category = 'Adventure'
    elif age <= 14:
        category = 'Mystery'
    elif age <= 18:
        category = 'Sci-Fi'
    else:
        category = 'Classics'
    points = (age ** 1.5) / 2
    vowels = 'aeiou'
    vowel_included = False
    for vowel in vowels:
        if vowel in name[0:3]:
            vowel_included = True
            break
    if vowel_included and age < 15:
        badge = True
    if name[-1].lower() in vowels and age % 2 == 0:
        bookmark = True


    print(f'Welcome {name}, your category will be {category}')
    print(f'You have {points:.2f} points.')
    if badge and bookmark:
        print(f'Congratulations, you have earned a badge and a bookmark!')
    elif badge:
        print(f'Congratulations, you have earned a badge!')
    elif bookmark:
        print(f'Congratulations, you have earned a bookmark!')
    print(f"It's a pleasure to have you with us {name[0].upper()+name[-1].upper()}!")

