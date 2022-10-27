input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    temp = array[0]
    for i in array:
        if temp <= i:
            temp = i
    return temp

result = find_max_num(input)
print(result)