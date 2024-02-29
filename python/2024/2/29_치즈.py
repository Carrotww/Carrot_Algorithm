# https://www.acmicpc.net/problem/2636

def make_outline():
    global outline_graph
    queue = deque([[0, 0]])
    outline_graph = [[0] * c for _ in range(r)]
    outline_graph[0][0] = 1
    while queue:
        cur_r, cur_c = queue.popleft()
        for d in range(4):
            n_r, n_c = cur_r+dr[d], cur_c+dc[d]
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
                continue
            if graph[n_r][n_c] == 0 and outline_graph[n_r][n_c] == 0:
                outline_graph[n_r][n_c] = 1
                queue.append([n_r, n_c])
    return outline_graph

def melt():
    new_graph = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 1 and check(i, j):
                new_graph[i][j] = 1

    return new_graph

# return true -> cheeze is not outside
def check(cur_r, cur_c):
    for d in range(4):
        n_r, n_c = cur_r + dr[d], cur_c + dc[d]
        if outline_graph[n_r][n_c] == 1:
            return False
    return True

if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    r, c = map(int, input().split())
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    graph = []
    total = 0
    for _ in range(r):
        t = list(map(int, input().split()))
        total += sum(t)
        graph.append(t)

    visited = [[0] * c for _ in range(r)]
    cnt = 0
    result = [total]
    
    while total:
        outline_graph = make_outline()
        graph = melt()
        cnt += 1
        total = 0
        for i in range(r):
            total += sum(graph[i])
        result.append(total)

    print(cnt)
    print(result[-2])


