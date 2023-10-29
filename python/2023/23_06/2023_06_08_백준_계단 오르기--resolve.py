# https://www.acmicpc.net/problem/2579

def solve():
    import sys
    N = int(sys.stdin.readline())
    scores = [0] * (N+1)
    dp = [0] * (N+1)

    for i in range(1, N+1):
        scores[i] = int(sys.stdin.readline())
    
    dp[1] = scores[1]
    if N >= 2:
        dp[2] = scores[1] + scores[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])
    
    print(dp[N])

if __name__ == "__main__":
    solve()