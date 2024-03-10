# https://www.acmicpc.net/problem/2792

def check(num):
    can_give = 0
    for j_cnt in jary:
        cnt = (j_cnt + num - 1) // num
        can_give += cnt
    return can_give <= n

def binary_search():
    start, end = 1, max(jary)
    result = end
    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    jary = []
    for _ in range(m):
        jary.append(int(input()))

    print(binary_search())

