# https://www.acmicpc.net/problem/11003

def solve():
    import sys

    N, L = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    result = []

    temp = 0
    for idx, num in enumerate(a):
        if num < temp:
            result.append(temp)
            continue
        start = idx - L + 1
        end = idx
        if start < 0:
            start = 0
        temp = min(a[start:end+1])
        result.append(temp)

    print(' '.join([str(x) for x in result]))

if __name__ == "__main__":
    solve()