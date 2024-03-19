# https://www.acmicpc.net/problem/9252

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    a = input().rstrip()
    b = input().rstrip()

    dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    visited = [[''] * (len(b)+1) for _ in range(len(a)+1)]

    cnt = 0
    result = ''
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                visited[i][j] = visited[i-1][j-1] + a[i-1]
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                    visited[i][j] = visited[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
                    visited[i][j] = visited[i][j-1]

            if cnt < dp[i][j]:
                result = visited[i][j]
                cnt = dp[i][j]

    print(dp[-1][-1])
    if dp[-1][-1]:
        print(visited[-1][-1])

