# https://www.acmicpc.net/problem/11722

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    ary = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if ary[i] < ary[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))

