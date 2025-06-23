
#  file checker

# file = input('Enter the file name: ')
# if file.endswith('.txt'):
#     print(f'The file {file} is a text file.')
# elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
#     print(f'The file {file} is an image file.')
# elif file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.doc'):
#     print(f'The file {file} is a document file.')
# else:
#     print('The file type is unknown.')


# phrase = input('Enter a phrase: ')
# slices = phrase.split()
# print(slices)


# word = input('Enter a word: ')
# print(word.strip(' '))
# word = word.replace(' ', '')
# if word == word[::-1]:
#     print(f'The word {word} is a palindrome.')
# else:
#     print(f'The word {word} is not a palindrome.')



# Sum of even and odd numbers from a string
# numbers = '78,12,34,32,45,67,1, and 89'.replace(' and ', '').split(',')
# even_sum  = 0
# odd_sum = 0
# for num  in numbers:
#     if int(num) % 2 == 0:
#         even_sum += int(num)
#     else:
#         odd_sum += int(num)
# print(f'The sum of even numbers is {even_sum}')
# print(f'The sum of odd numbers is {odd_sum}')


students = "Jeffrey, Afia, Lily, James, Dogbey, Emmanuel, Kofi, Janet, Phoeby and Adwoa"
students_list = students.replace(' and ', ', ').split(', ')
teams = []
for i in range(0,int(len(students_list)),2):
 teams.append(f'{students_list[i]} and {students_list[i+1]}')
for team in teams:
 print(team)