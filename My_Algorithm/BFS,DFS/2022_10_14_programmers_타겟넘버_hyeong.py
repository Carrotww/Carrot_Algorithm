# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    result = []
    
    def dfs(number, temp):
        if not number:
            if temp == target:
                result.append(1)
            return
        temp_num = number.pop()
        dfs(number[:], temp + temp_num)
        dfs(number[:], temp - temp_num)
    
    num = numbers.pop()
    dfs(numbers[:], -num)
    dfs(numbers[:], num)
    
    return len(result)

"""
# 프로그래머스 1등 풀이
# 제출 함수 자체를 재귀로 만든 답안

def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
"""