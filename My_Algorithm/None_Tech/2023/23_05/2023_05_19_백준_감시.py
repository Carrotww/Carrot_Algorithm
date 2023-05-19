# https://www.acmicpc.net/problem/15683

def solve():
    import sys
    import copy

    N, M = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    cctv = []
    for r in range(N):
        for c in range(M):
            if graph[r][c] != 0 and graph[r][c] != 6:
                cctv.append([r, c, graph[r][c]])

    cctv.sort(key=lambda x: x[2])

    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    cctv_direct = [
        [],
        [[0], [1], [2], [3]],
        [[0, 1], [2, 3]],
        [[0, 2], [0, 3], [1, 2], [1, 3]],
        [[0, 2, 3], [1, 2, 3], [0, 1, 2], [0, 1, 3]],
        [[0, 1, 2, 3]]
    ]

    def check(r, c, visited, direct):
        for i in direct:
            n_r, n_c = r+dr[i], c+dc[i]
            while (n_r >= 0 and n_r < N) and (n_c >= 0 and n_c < M) and visited[n_r][n_c] != 6:
                if visited[n_r][n_c] == 0:
                    visited[n_r][n_c] = '#'
                n_r, n_c = n_r+dr[i], n_c+dc[i]

    def check_result(graph):
        result = 0
        for r in range(N):
            for c in range(M):
                if graph[r][c] == 0:
                    result += 1
        return result

    result = float('inf')

    def dfs(graph, idx):
        nonlocal result
        if idx == len(cctv):
            result = min(result, check_result(graph))
            return
        cur_r, cur_c, cur_cctv_num = cctv[idx]
        for i in cctv_direct[cur_cctv_num]:
            temp_graph = copy.deepcopy(graph)
            check(cur_r, cur_c, temp_graph, i)
            dfs(temp_graph, idx+1)

    dfs(graph, 0)
    print(result)

if __name__ == "__main__":
    solve()