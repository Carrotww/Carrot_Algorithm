# https://www.acmicpc.net/problem/2644

def dfs(node, cnt):
    if node == b:
        return cnt

    for n_node in graph[node]:
        if visited[n_node] == 0:
            visited[n_node] = 1
            result = dfs(n_node, cnt + 1)
            if result != -1:
                return result

    return -1


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    a, b = map(int, input().split())
    m = int(input())

    visited = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited[a] = 1
    result = dfs(a, 0)
    print(result)
