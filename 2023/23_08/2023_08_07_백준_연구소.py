# https://www.acmicpc.net/problem/14502

def bfs(bfs_graph):
    from collections import deque
    queue = deque(start)
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    check_safe_zone = safe_zone - 3
    while queue:
        cur_r, cur_c = queue.popleft()
        for direct in range(4):
            n_r, n_c = cur_r+dr[direct], cur_c+dc[direct]
            if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= m) or bfs_graph[n_r][n_c] != 0:
                continue
            bfs_graph[n_r][n_c] = 2
            check_safe_zone -= 1
            queue.append([n_r, n_c])
    
    global result
    result = max(check_safe_zone, result)


def make_wall(cnt):
    import copy

    if cnt == 3:
        bfs(copy.deepcopy(graph))
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt+1)
                graph[i][j] = 0

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    graph = []
    start = []
    safe_zone = 0
    result = 0
    for r in range(n):
        temp = list(map(int, input().split()))
        graph.append(temp)
        for c in range(len(temp)):
            if temp[c] == 2:
                start.append([r, c])
            elif temp[c] == 0:
                safe_zone += 1
    
    make_wall(0)
    print(result)