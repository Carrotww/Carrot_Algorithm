# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    temp = [1 for _ in range(n + 2)]
    temp[0] = 0
    temp[-1] = 0
    for lo in lost:
        temp[lo] = 0
    
    for re in reserve:
        if temp[re] == 0:
            temp[re] = 1
            continue
        temp[re] = 2
    
    for i in range(1, n + 1):
        if temp[i] == 0:
            if temp[i-1] == 2:
                temp[i-1] -= 1
                temp[i] = 1
            elif temp[i+1] == 2:
                temp[i+1] -= 1
                temp[i] = 1

    return sum([1 for x in temp if x != 0])

    # n_lost = [x for x in range(1, n + 1) if temp[x] == 0]

    # for lo in n_lost:
    #     if temp[lo-1] == 2:
    #         temp[lo-1] = 1
    #         temp[lo] = 1
    #     elif temp[lo+1] == 2:
    #         temp[lo+1] = 1
    #         temp[lo] = 1

    # return sum([1 for x in temp if x != 0])
    
   
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))