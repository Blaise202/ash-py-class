# part1
shopping_list = [] #1
items = input('Enter the items separated by a comma(,): ') #2
items = items.split(',') #3
for item in items:
  shopping_list.append(item.strip())
print(shopping_list) #4
print('first item: ',shopping_list[0]) #5
print('last item: ',shopping_list[-1])

# Part2
new_item = input("Enter the other item: ")#1
shopping_list.insert(1, new_item) 
essentials = ['bread', 'rice', 'eggs', 'Milk', 'Honey'] #2
shopping_list.extend(essentials) 
print(shopping_list)
search = input('Search for the item: ') #3
try:
  shopping_list.remove(search)
  print(f'{search} was removed from your shopping list')
except:
  print(f'{search} is not in your shopping list')
print(shopping_list)

try: #4
  print(f'The last Item is: {shopping_list.pop()}')
  print(shopping_list)
  print(f'The first Item is: {shopping_list.pop(0)}')
  print(shopping_list)
except:
  print("Can't remove any item. the shopping list is empty")

try: #5
  del shopping_list[2]
  print(shopping_list)
except:
  print(f'Cannot delete 3rd item, only {len(shopping_list)} item(s) available.')

print(f' The first 3 items: {shopping_list[:3]}') #6

# part3
print('Items in shopping list: ') #1
i = 1
for item in shopping_list:
  print(f"{i}. {item}")
  i += 1

while True: #2
  choice = input("Do you want to add another item? (yes/no): ")
  if choice.lower() == "yes":
    new_item = input("Enter the item to add: ")
    shopping_list.append(new_item.strip())
  elif choice.lower() == "no":
    print('Loop exited')
    break
  else:
    print("Invalid input. Please type 'yes' or 'no'.")
print("Shopping list after while loop additions: ", shopping_list)

if not shopping_list: #3
  print("Your shopping list is currently empty.")
else:
  print(f"You have {len(shopping_list)} items in your shopping list.")

search = input("Search for item: ") #4
if search.strip() in shopping_list:
  print(f"'{search.strip()}' found in the shopping list.")
else:
  print(f"'{search.strip()}' not found in the shopping list.")