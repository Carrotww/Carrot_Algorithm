# https://www.acmicpc.net/problem/2467

def solve():
    import sys
    input = sys.stdin.readline

    n = int(input())
    solution_list = list(map(int, input().split()))
    solution_list.sort()

    start, end = 0, n-1
    nsum = float('inf')
    result = []

    while start < end:
        cur_sum = solution_list[start] + solution_list[end]

        if abs(cur_sum) < nsum:
            nsum = abs(cur_sum)
            result = [solution_list[start], solution_list[end]]

        if cur_sum < 0:
            start += 1
        else:
            end -= 1

    print(result[0], result[1])


if __name__ == "__main__":
    solve()
