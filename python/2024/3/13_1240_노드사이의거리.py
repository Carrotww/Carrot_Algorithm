# https://www.acmicpc.net/problem/1240

def dj(node):
    visited = [0] * (n + 1)
    queue = deque([node])
    visited[node] = 0
    while queue:
        cur_node = queue.popleft()
        for n_node, cost in graph[cur_node]:
            if visited[n_node] == 0 or visited[n_node] > visited[cur_node] + cost:
                visited[n_node] = visited[cur_node] + cost
                queue.append(n_node)
    return visited

if __name__ == "__main__":
    import sys
    from collections import defaultdict, deque
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(n-1):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    result = [0] * (n + 1)
    for i in range(1, n+1):
        result[i] = dj(i)

    for _ in range(m):
        a, b = map(int, input().split())
        print(result[a][b])

