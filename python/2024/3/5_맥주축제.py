# https://www.acmicpc.net/problem/17503

def check(cur_alcol):
    total_priority = 0
    day = 0
    for priority, alcol in ary:
        if alcol <= cur_alcol:
            total_priority += priority
            day += 1
            if day >= n:
                break
    if total_priority >= m and n == day:
        return True
    return False


def binarysearch(min_alcol, max_alcol):
    global result
    while min_alcol <= max_alcol:
        mid_alcol = (min_alcol + max_alcol) // 2
        if check(mid_alcol):
            result = min(result, mid_alcol)
            max_alcol = mid_alcol - 1
        else:
            min_alcol = mid_alcol + 1


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    ary = []
    min_alcol, max_alcol = float('inf'), -1

    for _ in range(k):
        priority, alcol = map(int, input().split())
        ary.append([priority, alcol])
        min_alcol = min(min_alcol, alcol)
        max_alcol = max(max_alcol, alcol)
    ary.sort(key=lambda x:-x[0])

    result = float('inf')
    binarysearch(min_alcol, max_alcol)
    if result == float('inf'):
        print(-1)
    else:
        print(result)

