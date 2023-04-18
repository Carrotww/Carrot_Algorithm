# https://www.acmicpc.net/problem/1806

def solve():
    import sys
    N, S = map(int, sys.stdin.readline().split())
    num_list = list(map(int, sys.stdin.readline().split()))

    left, right = 0, 0
    min_len = 100001
    total = num_list[0]
    while right < N and left <= right:
        if total >= S:
            min_len = min(min_len, right - left + 1)
            total -= num_list[left]
            left += 1
        else:
            right += 1
            if right < N:
                total += num_list[right]

    if min_len == 100001:
        print(0)
    else:
        print(min_len)

if __name__ == "__main__":
    solve()