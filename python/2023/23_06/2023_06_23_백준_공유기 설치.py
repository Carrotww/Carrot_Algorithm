# https://www.acmicpc.net/problem/2110

def solve():
    import sys
    input = sys.stdin.readline
    n, c = map(int, input().split())
    home_list = []
    for _ in range(n):
        home_list.append(int(input()))
    home_list.sort()

    start, end = 1, home_list[-1] - home_list[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        cur_position = home_list[0]

        for i in range(1, n):
            if home_list[i] >= cur_position + mid:
                cnt += 1
                cur_position = home_list[i]
        if cnt >= c:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(result)

if __name__ == "__main__":
    solve()