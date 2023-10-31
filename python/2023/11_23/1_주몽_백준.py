# https://www.acmicpc.net/problem/1940

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    ary = list(map(int, input().split()))
    ary.sort()

    result = 0
    left, right = 0, n - 1
    while left < right:
        cur_val = ary[left] + ary[right]
        if cur_val == m:
            result += 1
            left += 1
            right -= 1
        elif cur_val > m:
            right -= 1
        else:
            left += 1
    print(result)

