
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


word = input('Enter a word: ')
print(word.strip(' '))
word = word.replace(' ', '')
if word == word[::-1]:
    print(f'The word {word} is a palindrome.')
else:
    print(f'The word {word} is not a palindrome.')



