# https://www.acmicpc.net/problem/7795

def lowerbound(a_size, ary):
    start, end = 0, len(ary)
    while start < end:
        mid = (start + end) // 2
        if ary[mid] < a_size:
            start = mid + 1
        else:
            end = mid
    return start

def solve():
    a, b = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    total = 0

    for i in range(len(a)):
        total += lowerbound(a[i], b)

    return total

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    t = int(input())
    result = []
    for _ in range(t):
        r = solve()
        result.append(r)

    for r in result:
        print(r)

