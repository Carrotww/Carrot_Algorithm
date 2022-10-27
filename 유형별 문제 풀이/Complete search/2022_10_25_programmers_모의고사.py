# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    pick_val = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    result = [0, 0, 0]
    
    for i in range(3):
        temp = pick_val[i]
        viv = len(answers) // len(temp)
        if viv != 0:
            temp *= viv
        for x, y in list(zip(temp, answers)):
            if x == y:
                result[i] += 1
    return [num for num, key in enumerate(result, start=1) if key == max(result)]