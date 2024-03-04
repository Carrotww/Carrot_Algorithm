# https://www.acmicpc.net/problem/19637

def upperbound(target):
    start, end = 0, n
    while start < end:
        mid = (start + end) // 2
        if ary[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    ary = []
    check = {}
    for _ in range(n):
        a, b = input().split()
        ary.append(int(b))
        if int(b) in check:
            continue
        check[int(b)] = a

    result = []
    for _ in range(m):
        index = upperbound(int(input()))
        result.append(check[ary[index]])

    for r in result:
        print(r)

