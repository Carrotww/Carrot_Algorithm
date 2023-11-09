# https://www.acmicpc.net/problem/12865

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    ary = []
    for _ in range(n):
        ary.append(list(map(int, input().split())))
    # row -> n ; col -> w
    dp = [[0] * (k+1) for _ in range(n)]
    for i in range(n):
        w, v = ary[i]
        for j in range(1, k+1):
            if j < w:
                if i == 0:
                    continue
                dp[i][j] = dp[i-1][j]
            else:
                if i == 0:
                    dp[i][j] = v
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

    from pprint import pprint
    pprint(dp)
    print(dp[-1][-1])
