# https://www.acmicpc.net/problem/19637

def binery_search(num):
    start, end = 0, n-1
    while start < end:
        mid = (start + end) // 2
        if ary[mid] < num:
            start = mid + 1
        else:
            end = mid
    return check[ary[end]]

def upperbound(target):
    start, end = 0, n
    while start < end:
        mid = (start + end) // 2
        if ary[mid] < target:
            start = mid + 1
        else:
            end = mid
    if target == ary[end]:
        return target
    else:
        return ary[end+1]

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    ary = []
    check = {}
    for _ in range(n):
        a, b = input().split()
        ary.append(int(b))
        check[int(b)] = a

    result = []
    for _ in range(m):
        val = upperbound(int(input()))
        result.append(check[val])

    for r in result:
        print(r)

