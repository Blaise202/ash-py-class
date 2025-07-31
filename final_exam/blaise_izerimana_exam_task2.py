def pivot_shuffle(data, k):
    left = data[0:k]
    middle = data[k:2*k]
    data.reverse()
    right = data[0:k]
    right.reverse()
    print(left, middle, right)
    shuffled_list = right
    shuffled_list.extend(middle)
    shuffled_list.extend(left)
    print(shuffled_list)
    left = shuffled_list[0:k]
    rest_items = shuffled_list[k:]
    left.reverse()
    left.extend(rest_items)
    new_list = left
    print(new_list)
    list_with_no_duplicates = []
    for i in new_list:
        if i not in list_with_no_duplicates:
            list_with_no_duplicates.append(i)
    return 