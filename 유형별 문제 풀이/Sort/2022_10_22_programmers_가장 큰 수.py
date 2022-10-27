# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x * 3, reverse=True)
    return str(int(''.join(numbers)))

"""
# 틀린 답안 왜 틀렸는지 아직 모르겠음
def solution(numbers):
    result = []
    numbers = list(map(str, numbers))
    for i in range(len(numbers)):
        temp = numbers[i]
        while len(temp) < 4:
            temp += numbers[i][0]
        result.append((numbers[i], temp))
    result = sorted(result, key=lambda x:x[1], reverse=True)
    return ''.join([x[0] for x in result])
"""

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))