# https://www.acmicpc.net/problem/1260

def solve():
    import sys
    from collections import deque, defaultdict
    
    N, E, start_node = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(E):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)
    
    for i in graph.values():
        i.sort()

    result_dfs = []
    result_bfs = []

    visited = [-1 for _ in range(N+1)]
    visited[start_node] = 1

    def dfs(node):
        result_dfs.append(node)
        for n_node in graph[node]:
            if visited[n_node] == 1:
                continue
            visited[n_node] = 1
            dfs(n_node)

    def bfs():
        queue = deque()
        visited = [-1 for _ in range(N+1)]
        visited[start_node] = 1
        queue.append(start_node)

        while queue:
            cur_node = queue.popleft()
            result_bfs.append(cur_node)
            for n_node in graph[cur_node]:
                if visited[n_node] == 1:
                    continue
                visited[n_node] = 1
                queue.append(n_node)

    dfs(start_node)
    bfs()

    result_dfs = [str(x) for x in result_dfs]
    result_bfs = [str(x) for x in result_bfs]

    print(' '.join(result_dfs))
    print(' '.join(result_bfs))
    
if __name__ == "__main__":
    solve()