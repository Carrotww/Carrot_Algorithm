# https://www.acmicpc.net/problem/1932

# 1번째 풀이
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = graph[0][0]

    # 행
    for i in range(n-1):
        # 열
        for j in range(i+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+graph[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+graph[i+1][j+1])

    print(max(dp[-1]))


# 2번째 풀이
def solve():
    import sys
    N = int(sys.stdin.readline())
    dp = []
    for i in range(N):
        dp.append(list(map(int, sys.stdin.readline().split())))

    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

    print(max(dp[N-1]))

if __name__ == "__main__":
    solve()