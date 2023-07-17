# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    result = []

    for com in commands:
        temp = array[com[0]-1:com[1]]
        temp.sort()
        result.append(temp[com[2]-1])
        
    return result

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))