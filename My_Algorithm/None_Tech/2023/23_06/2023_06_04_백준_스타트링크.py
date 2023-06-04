# https://www.acmicpc.net/problem/5014

def solve():
    import sys
    from collections import deque
    total, start, end, up, down = map(int, sys.stdin.readline().split())
    dp = [float('inf')] * (total + 1)
    dp[start] = 0
    queue = deque()
    queue.append([start, 0])

    while queue:
        cur_node, cnt = queue.popleft()
        if cur_node == end:
            print(cnt)
            return
        up_node = cur_node + up
        if 1 <= up_node <= total and dp[up_node] > cnt+1:
            dp[up_node] = cnt+1
            queue.append([up_node, cnt+1])
        down_node = cur_node - down
        if 1 <= down_node <= total and dp[down_node] > cnt+1:
            dp[down_node] = cnt+1
            queue.append([down_node, cnt+1])
    print('use the stairs')


if __name__ == "__main__":
    solve()
