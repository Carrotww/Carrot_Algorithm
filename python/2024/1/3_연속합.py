# https://www.acmicpc.net/problem/1912

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    ary = list(map(int, input().split()))

    dp = [0] * n
    dp[0] = ary[0]
    result = dp[0]
    for i in range(1, n):
        if ary[i] >= dp[i-1]:
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + ary[i]
            else:
                dp[i] = ary[i]
        else:
            dp[i] = dp[i-1] + ary[i]
        if dp[i] > result:
            result = dp[i]
    print(result)
