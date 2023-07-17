# https://www.acmicpc.net/problem/11066

def solve():
    import sys
    input = sys.stdin.readline

    test_case = int(input())

    for _ in range(test_case):
        n = int(input())
        files = list(map(int, input().split()))
        dp = [[0] * n for _ in range(n)]
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                min_val = float('inf')
                for k in range(j-i):
                    min_val = min(min_val, dp[i][i+k] + dp[i+k+1][j])
                dp[i][j] = min_val + sum(files[i:j+1])
        print(dp[0][n-1])

if __name__ == "__main__":
    solve()
