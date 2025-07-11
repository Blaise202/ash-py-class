# part1
shopping_list = [] #1
items = input('Enter the items separated by a comma(,): ') #2
items = items.split(',') #3
for item in items:
 shopping_list.append(item.strip())
print(shopping_list) #4
print('first item: ',shopping_list[0]) #5
print('last item: ',shopping_list[-1])

# part2
new_item = input("Enter the other item: ")
shopping_list.insert(1, new_item) #1
essentials = ['bread', 'rice', 'eggs', 'Milk', 'Honey'] #2
shopping_list.extend(essentials) 
print(shopping_list);
search = input('Search for the item: ')
try:
  shopping_list.remove(search)
  print(f'{search} was removed from your shopping list')
except:
  print(f'{search} is not in your shopping list')
print(shopping_list);

