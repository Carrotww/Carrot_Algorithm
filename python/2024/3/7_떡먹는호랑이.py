# https://www.acmicpc.net/problem/2502

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    d, k = map(int, input().split())
    dp = [[0, 0] for _ in range(d+1)]
    dp[1][0] = 1
    dp[2][1] = 1
    for i in range(3, d+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

    x, y = dp[d][0], dp[d][1]
    is_found = False
    for i in range(k // x):
        for j in range(k // y):
            if x * i + y * j == k:
                is_found = True
                break
            elif x * i + y * j > k:
                break
        if is_found:
            break
    print(i)
    print(j)
                

