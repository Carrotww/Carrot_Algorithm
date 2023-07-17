# https://www.acmicpc.net/problem/12865

def solve():
    import sys
    
    N, K = map(int, sys.stdin.readline().split())
    dp = [[0]*(K+1) for _ in range(N+1)]
    thing_list = [[0, 0]]
    for _ in range(N):
        thing_list.append(list(map(int, sys.stdin.readline().split())))

    for i in range(1, N+1):
        for j in range(1, K+1):
            w = thing_list[i][0]
            v = thing_list[i][1]

            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], v+dp[i-1][j-w])
    
    print(dp[N][K])

if __name__ == "__main__":
    solve()