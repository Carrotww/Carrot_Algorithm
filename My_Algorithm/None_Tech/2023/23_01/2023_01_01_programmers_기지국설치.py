# https://school.programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):
    result = 0
    total_range = 2 * w + 1
    start = 1
    for st in stations:
        width = st - w
        if width <= start:
            continue
        cnt = 1
        cur_range = total_range
        while cur_range < width - 1:
            cur_range += cur_range
            cnt += 1
        result += cnt
    last_range = n - stations[-1] - w
    cnt = 1
    while total_range < last_range - 1:
        total_range += total_range
        cnt += 1
    
    return result + cnt

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))