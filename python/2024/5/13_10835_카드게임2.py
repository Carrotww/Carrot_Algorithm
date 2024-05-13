# https://www.acmicpc.net/problem/10835

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    dp = [[-1] * (n+1) for _ in range(n+1)]
    dp[0][0] = 0
    result = 0

    for i in range(n):
        for j in range(n):
            if dp[i][j] != -1:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
                if left[i] > right[j]:
                    dp[i][j+1] = max(dp[i][j+1], dp[i][j]+right[j])

    for i in range(n+1):
        for j in range(n+1):
            result = max(result, dp[i][j])

    print(result)

