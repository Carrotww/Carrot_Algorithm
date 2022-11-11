# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    result = []
    for i, j, k in commands:
        result.append(sorted(array[i-1:j])[k-1])
    return result