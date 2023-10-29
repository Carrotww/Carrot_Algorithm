# https://www.acmicpc.net/problem/11053

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    ary = list(map(int, input().split()))

    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if ary[i] > ary[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
