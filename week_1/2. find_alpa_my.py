from collections import defaultdict

input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    result = defaultdict(int)
    string = ''.join(string.split())
    for i in string:
        result[i] += 1
    test = [[key, val] for key, val in result.items()]
    temp = test[0]

    for x, y in test:
        if temp[1] <= y:
            temp[0], temp[1] = x, y

    return temp[0]
result = find_max_occurred_alphabet(input)
print(result)