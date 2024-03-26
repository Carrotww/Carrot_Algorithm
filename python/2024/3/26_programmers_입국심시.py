# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def check(cur_time, times, n):
    total = 0
    for t in times:
        total += cur_time // t

    return total >= n

def solution(n, times):
    result = float('inf')

    start, end = 1, n * max(times)
    while start <= end:
        mid = (start + end) // 2

        # 만약 검사하기 시간이 충분하다면 시간을 줄인다
        if check(mid, times, n):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1

    return result

