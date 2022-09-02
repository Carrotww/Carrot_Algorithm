from collections import defaultdict

input = "abadabac"


def find_not_repeating_character(string):
    temp = defaultdict(int)
    for char in string:
        temp[char] += 1
    for key, val in temp.items():
        if val == 1:
            return key
        else:
            return 'noting'


result = find_not_repeating_character(input)
print(result)
