# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    cnt = 0
    lost_temp = [x for x in lost if x not in reserve]
    reserve_temp = [x for x in reserve if x not in lost]

    lost_temp.sort()
    reserve_temp.sort()
    
    for lo in lost_temp:
        for i in range(len(reserve_temp)):
            if lo - 1 == reserve[i] or lo + 1 == reserve[i]:
                reserve[i] = -1
                break
        else:
            cnt += 1
    
    return n - cnt

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))