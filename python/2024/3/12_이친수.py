# https://www.acmicpc.net/problem/2193

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    if n == 1 or n == 2:
        print(1)
        exit(0)
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = 1
        for j in range(i-1):
            dp[i] += dp[j]
    print(dp[n])

