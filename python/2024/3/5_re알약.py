# https://www.acmicpc.net/problem/4811

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    dp = [[0] * 32 for _ in range(32)]

    for i in range(32):
        dp[0][i] = 1

    for i in range(1, 31):
        for j in range(31):
            if j == 0:
                dp[i][0] = dp[i-1][1]
            else:
                dp[i][j] = dp[i-1][j+1] + dp[i][j-1]

    while 1:
        num = int(input())
        if num == 0:
            break
        print(dp[num][0])

