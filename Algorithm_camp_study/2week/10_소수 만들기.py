# https://school.programmers.co.kr/learn/courses/30/lessons/12977?language=python3

def check(num):
    if num == 1:
        return 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return 0
    return 1

def solution(nums):
    from itertools import combinations
    result = 0
    
    temp_list = combinations(nums, 3)
    for i in temp_list:
        result += check(sum(i))
    return result