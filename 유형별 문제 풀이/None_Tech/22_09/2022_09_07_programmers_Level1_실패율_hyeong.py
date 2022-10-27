# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    result = {}
    total = len(stages)

    for i in range(1, N + 1):
        if total != 0:
            current_n = stages.count(i)
            result[i] = current_n / total
            total -= current_n
        else:
            result[i] = 0
    
    result = sorted(result, key=lambda x :result[x], reverse=True)
    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))