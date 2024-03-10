# https://www.acmicpc.net/problem/22857

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    ary = list(map(int, input().split()))

    start, end = 0, 0
    result = 0
    odd_cnt = 0
    for start in range(n):
        while end < n and odd_cnt <= k:
            if ary[end] % 2 != 0:
                odd_cnt += 1
            end += 1
        result = max(result, end - start - odd_cnt)
        if ary[start] % 2 != 0:
            odd_cnt -= 1
    print(result)

