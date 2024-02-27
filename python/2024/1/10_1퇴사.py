# https://www.acmicpc.net/problem/14501

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    ary = []
    for _ in range(n):
        ary.append(tuple(map(int, input().split())))

    dp = [0] * (n + 1)

    for i in range(n):
        for j in range(i+ary[i][0], n+1):
            if dp[j] < dp[i] + ary[i][1]:
                dp[j] = dp[i] + ary[i][1]

    print(dp[-1])

