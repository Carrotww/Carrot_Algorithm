import copy

input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    a, b = 0, 0
    string = list(string)
    temp = copy.deepcopy(string)
    temp2 = copy.deepcopy(string)

    for i in range(len(temp)): # 1로 바꿈
        if '0' not in temp:
            break
        if temp[i] == '0':
            temp[i] = '1'
            x = 1
            while x != len(temp) and i != len(temp) - 1:
                if temp[i + x] == '0':
                    temp[i + x] = '1'
                    x += 1
                if temp[i + x] == '1':
                    break
            a += 1
    for i in range(len(temp)): # 0으로 바꿈
        if '1' not in temp2:
            break
        if temp2[i] == '1':
            temp2[i] = '0'
            x = 1
            while x != len(temp) and i != len(temp) - 1:
                if temp2[i + x] == '1':
                    temp2[i + x] = '0'
                    x += 1
                if temp2[i + x] == '0':
                    break
            b += 1

    return min(a, b)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)