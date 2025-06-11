vowels = 'aeiouAEIOU'
word = input("Enter a word: ")
if len(word) > 5 and word.isalpha():
    print("The word is longer than 5 characters and contains only letters.")
    if word[0] in vowels and word[-1] not in vowels:
        print("The word starts with a vowel and ends with a consonant.")
    else:
        print("First condition failed")
    if word.isupper() and 'z' in word.lower():
        print("The word is in uppercase and contains the letter 'z'.")
    else:
        print("Second condition failed")
else:
    print("The word does not meet the criteria.")
