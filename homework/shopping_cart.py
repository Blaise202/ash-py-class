def is_shopping_list_empty(shopping_list): #a
    if len(shopping_list) == 0:
        return True
    return False


def add_item(item, shopping_list): #b
    shopping_list.append(item.strip())
    return shopping_list

def remove_item_by_name(item, shopping_list): #c
    if is_shopping_list_empty(shopping_list):
        return 'The shopping list is empty.'
    try:
        shopping_list.remove(item.strip())
    except:
        return 'item not found'
    return shopping_list


def extend_shopping_list(shopping_list, new_list): #d
    if is_shopping_list_empty(new_list):
        return 'the new list is empty'
    shopping_list.extend(new_list)
    return shopping_list


def delete_item_by_index(index, shopping_list):#e
    if is_shopping_list_empty(shopping_list):
        return 'The shopping list is empty'
    try:
        del shopping_list[index]
    except:
        return 'the index is not in the range'
    return shopping_list

def delete_print_item(index, shopping_list):#f
    if is_shopping_list_empty(shopping_list):
        return 'The shopping list is empty'
    try:
        item = shopping_list.pop(index)
        print(f'The deleted item is {item}.')
    except IndexError:
        return 'the index is not in the range'
    return shopping_list


def sub_shopping_list(start_index, end_index, shopping_list): #g
    if is_shopping_list_empty(shopping_list):
        print('The shopping list is empty')
    else:
        x = len(shopping_list[start_index:end_index])
        new_list = shopping_list[start_index:end_index]
        print(f"The sub-list from index {start_index} to {end_index-1} has: {x} items and they are {new_list}")

def print_shopping_list_items(shopping_list): #h
    if is_shopping_list_empty(shopping_list):
        return 'The shopping list is empty'
    print("The shopping list:")
    i = 0
    for item in shopping_list:
        i += 1
        print(f"{i}. {item}")

def insert_item(index, item, shopping_list):
    try:
        shopping_list.insert(index, item.strip())
        print(f"'{item.strip()}' inserted at index {index}.")
    except:
        print(f"Index {index} is out of bounds. Item appended instead.")
    return shopping_list

def total_items(shopping_list):
    return len(shopping_list)
