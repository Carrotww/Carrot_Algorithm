# https://www.acmicpc.net/problem/14501

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    ary = []
    for _ in range(n):
        ary.append(tuple(map(int, input().split())))

    dp = [0] * (n+1)

    for i in range(n-1, -1, -1):
        if i + ary[i][0] > n:
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+1], ary[i][1] + dp[i + ary[i][0]])

    print(dp[0])

