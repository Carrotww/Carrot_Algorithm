# https://www.acmicpc.net/problem/2135

import sys

def count_min_length(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    def get_length(x):
        if x > 99:
            return 3
        if x > 9:
            return 2
        return 1

    def check(i, j, d):
        if (j - i + 1) % d:
            return False
        for k in range(i + d, j + 1):
            if s[k] != s[k - d]:
                return False
        return True

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = length
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
            for d in range(1, length + 1):
                if check(i, j, d):
                    dp[i][j] = min(dp[i][j], get_length(length // d) + 2 + dp[i][i + d - 1])

    return dp[0][n - 1]

def solve():
    s = sys.stdin.readline().rstrip()
    print(count_min_length(s))

if __name__ == "__main__":
    solve()
