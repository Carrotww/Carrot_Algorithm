# https://school.programmers.co.kr/learn/courses/30/lessons/86051

import collections

def solution(numbers):
    result = 0
    check_dict = collections.defaultdict(list)
    for num in numbers:
        if num not in check_dict:
            check_dict[num].append(num)
    for i in range(1, 10):
        if i not in check_dict:
            result += i
    
    return result