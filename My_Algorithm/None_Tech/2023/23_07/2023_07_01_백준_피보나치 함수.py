# https://www.acmicpc.net/problem/1003

def solve():
    import sys
    input = sys.stdin.readline
    n = int(input())
    dp = [[0]*2 for _ in range(41)]
    dp[0] = [1, 0]
    dp[1] = [0, 1]

    for idx in range(2, len(dp)):
        dp[idx][0] = dp[idx-1][0] + dp[idx-2][0]
        dp[idx][1] = dp[idx-1][1] + dp[idx-2][1]

    for _ in range(n):
        cur_target_num = int(input())
        print(f'{dp[cur_target_num][0]} {dp[cur_target_num][1]}')

if __name__ == "__main__":
    solve()
