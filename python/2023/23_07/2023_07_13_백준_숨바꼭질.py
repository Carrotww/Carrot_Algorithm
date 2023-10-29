# https://www.acmicpc.net/problem/1697

# bfs
if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, k = map(int, input().split())
    dp = [float('inf')] * 100001
    dp[n] = 0
    queue = deque()
    queue.append(n)

    while queue:
        cur_po = queue.popleft()
        for i in range(3):
            if i == 0:
                n_po = cur_po - 1
            elif i == 1:
                n_po = cur_po + 1
            else:
                n_po = cur_po * 2

            if 0 <= n_po <= 100000 and dp[n_po] > dp[cur_po] + 1:
                dp[n_po] = dp[cur_po] + 1
                queue.append(n_po)

    print(dp[k])

# dp
if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    dp = [float('inf')] * 100001
    dp[n] = 0

    if n >= k:
        print(n-k)
    else:
        for i in range(n):
            dp[i] = n - i
        for i in range(n+1, k+1):
            if i % 2 == 0:
                temp = dp[i // 2] + 1
            else:
                temp = min(dp[(i+1)//2], dp[(i-1)//2]) + 2
                
            dp[i] = min(temp, dp[i-1]+1)
        print(dp[k])