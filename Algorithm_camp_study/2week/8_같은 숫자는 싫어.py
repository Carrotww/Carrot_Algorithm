# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    temp = -1
    result = []
    for i in range(len(arr)):
        if arr[i] == temp:
            continue
        temp = arr[i]
        result.append(temp)
    return result