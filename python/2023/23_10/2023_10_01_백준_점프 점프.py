# https://www.acmicpc.net/problem/11060

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    ary = list(map(int, input().split()))
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(n):
        start = i
        end = i + ary[i]
        if end >= n:
            end = n-1
        for j in range(start, end + 1):
            if dp[j] > dp[i] + 1:
                dp[j] = dp[i] + 1
    
    if dp[-1] == float('inf'):
        print(-1)
    else:
        print(dp[-1])