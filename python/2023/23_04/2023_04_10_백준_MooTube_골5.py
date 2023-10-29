# https://www.acmicpc.net/problem/15591

def dfs(k, node):
    for n_node, weight in graph[node]:
        # stack.append([n_node, min(weight, graph[])])
        pass
    
    return

def bfs(k, node):
    from collections import deque
    visited = [0] * (n + 1)
    queue = deque()
    queue.append(node)
    visited[node] = 1
    cnt = 0
    while queue:
        cur_node = queue.popleft()
        for n_node, weight in graph[cur_node]:
            if visited[n_node] == 1:
                continue
            if weight >= k:
                visited[n_node] = 1
                queue.append(n_node)
                cnt += 1
    return cnt

if __name__ == "__main__":
    import sys
    from collections import defaultdict
    result = []
    graph = defaultdict(list)
    n, q = map(int, sys.stdin.readline().split())

    for _ in range(n-1):
        start, end, weight = map(int, sys.stdin.readline().split())
        graph[start].append([end, weight])
        graph[end].append([start, weight])
    
    for _ in range(q):
        k, node = map(int, sys.stdin.readline().split())
        stack = []
        result.append(bfs(k, node))
    
    for re in result:
        print(re)