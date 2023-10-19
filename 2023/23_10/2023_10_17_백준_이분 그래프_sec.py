# https://www.acmicpc.net/problem/1707

def bfs(node):
    queue = deque([(node, 1)])
    visited[node] = 1
    while queue:
        cur_node, color = queue.popleft()
        for n_node in graph[cur_node]:
            if visited[n_node] == 0:
                queue.append((n_node, -color))
                visited[n_node] = -color
            elif visited[n_node] * color == 1:
                return False
    return True

if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    k = int(input())
    for _ in range(k):
        v, e = map(int, input().split())
        graph = [[] for _ in range(v+1)]
        visited = [0] * (v + 1)

        for _ in range(e):
            start, end = map(int, input().split())
            graph[start].append(end)
            graph[end].append(start)

        result = True
        for i in range(1, v+1):
            if visited[i] == 0:
                result = bfs(i)
                if result == False:
                    break

        if result:
            print('YES')
        else:
            print('NO')
