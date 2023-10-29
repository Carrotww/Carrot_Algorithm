# https://www.acmicpc.net/problem/9465

def solve():
    col = int(input())
    graph = []
    for _ in range(2):
        graph.append(list(map(int, input().split())))
    
    dp = [[0]*col for _ in range(2)]

    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]

    for c in range(1, col):
        for r in range(2):
            if r == 1:
                dp[r][c] = max(dp[0][c-1]+graph[r][c], dp[1][c-1])
            else:
                dp[r][c] = max(dp[1][c-1]+graph[r][c], dp[0][c-1])
    print(max(dp[1][-1], dp[0][-1]))

if __name__ == "__main__":
    import sys
    
    input = sys.stdin.readline
    n = int(input())

    for _ in range(n):
        solve()