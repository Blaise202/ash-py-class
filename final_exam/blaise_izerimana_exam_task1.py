# question 1
# task 1
def data_processing(responses):
    new_responses = []
    for response in responses:
        processed_response = response.strip().lower()
        if processed_response[0] in 'aeiou':
            new_responses.append(processed_response)
    return new_responses

# task 2

def split_responses(responses):
    responses = data_processing(responses)
    reports = []
    for entry in responses:
        separated_response = entry.split(':')
        name = separated_response[0]
        name = name[::-1]
        if(len(name) < 3):
            name_id = (3-len(name))*"x"+name
        elif(len(name) > 3):
            name_id = name[0:3]
        else:
            name_id = name
        name_id = name_id+str(len(name))
        answers = separated_response[1].split(',')
        if 'true' in answers or 'false' in answers:
            i = 0
            string_score = ''
            for answer in answers:
                if answer == 'true':
                    answers[i] = '1'
                else:
                    answers[i] = '0'
                i += 1
            lowest = min(answers)
            if(len(answers) > 1):
                answers.remove(lowest)
            for answer in answers:
                if answer == '1':
                    string_score += '1'
                else:
                    string_score += '0'
            maximum = len(answers)
            score_sum = 0
            for score in answers:
                score_sum += int(score)
            
        else:
            continue
        reports.append(f'{name_id}|{string_score}|{score_sum}/{maximum}')
    return reports


# question 2
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



data = [
 " Ama:True,False,True ",
 "eRIC:False,False,True",
 "Yaw:False,True,False",
 "Opoku:True",
 "eve:false,false,false,false"
]
print(split_responses(data))