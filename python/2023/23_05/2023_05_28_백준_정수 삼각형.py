# https://www.acmicpc.net/problem/1932

def solve():
    import sys
    N = int(sys.stdin.readline())
    dp = []
    for i in range(N):
        dp.append(list(map(int, sys.stdin.readline().split())))

    for i in range(1, N):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == len(dp[i]) - 1:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

    print(max(dp[N-1]))


if __name__ == "__main__":
    solve()