# for loop implementation of quaestion 1

password = "python123"
found = False

for i in range(3):
    if i == 0:
        attempt = input('Please enter the password: ')
    else:        
         attempt = input(f"Incorrect password. {3-i} attempt(s) remaining: ")
    if password == attempt:
        print('Access granted')
        found = True
        break
if not found:
    print("Access denied")



# while loop implementation of quaestion 2


attempts_allowed = 3
password = "python123"

found = False
while not found and attempts_allowed > 0:
    if attempts_allowed == 3:
        attempt = input('Please enter the password: ')
    else:        
        attempt = input(f"Incorrect password. {attempts_allowed} attempt(s) remaining: ")
    attempts_allowed -= 1
    if password == attempt:
        print('Access granted')
        found = True
        break
if not found:
    print("Access denied")




# implementation of quaestion 2


correct = False
trials = 0

attempt = input('Please enter the password: ')
while not correct:
    trials += 1
    if attempt == 'python123':
        print(f"After {trials} attempt(s), you’ve been granted access.")
        correct = True
    else:
        attempt = input('Incorrect password. Try again:')



# implementation of quaestion 3

numbers =  [12, 7, 9, 24, 31, 4, 18, 3, 5]
even_sum = 0
odd_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print(f'the sum of odd numbers is {odd_sum}')
print(f'the sum of even numbers is {even_sum}')
