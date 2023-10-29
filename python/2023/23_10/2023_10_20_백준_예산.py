# https://www.acmicpc.net/problem/2512

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    ary = list(map(int, input().split()))
    total = int(input())

    if sum(ary) <= total:
        print(max(ary))
    else:
        start, end = 0, max(ary)
        while start <= end:
            mid = (start + end) // 2
            t = 0
            for a in ary:
                if a < mid:
                    t += a
                else:
                    t += mid
            if t <= total:
                start = mid + 1
            else:
                end = mid - 1
        print(end)
