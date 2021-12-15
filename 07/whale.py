'''Make these crabs the same horizontal level with the fewest possible increments / decrements'''
input = [16,1,2,0,4,2,7,1,2,14]

# Find the most common number

def most_common(input):
    '''Find the most common item in a list'''
    if len(input) == 0 or input == None:
        return "Please supply a list of values"
    else:
        values_count = {}
        for i in input:
            if i in values_count.keys():
                values_count[i] += 1
            else:
                values_count.setdefault(i,1)
    most_common_value = [0,0]

    for value in values_count:
        if values_count[value] > most_common_value[1]:
            most_common_value[0] = value
            most_common_value[1] = values_count[value]
        
    return most_common_value[0]

def difference_of_value_to_most_common(value,target):
    sort  = sorted([value,target],reverse=True)
    return sort[0] - sort[1]



most = most_common(input)

shift_total = 0

for i in input:
    amount_shift = difference_of_value_to_most_common(i,most)
    shift_total += amount_shift

print(f"To align to horizontal positon {most} would take a total of {shift_total} with input values {input}")
