# https://www.acmicpc.net/problem/2133

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    if n % 2 == 1:
        print(0)
        exit(0)
    dp = [0] * (n + 1)
    if n >= 2:
        dp[2] = 3

    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * dp[2] + 2
        for j in range(2, i-2, 2):
            dp[i] += dp[j] * 2

    print(dp[n])


