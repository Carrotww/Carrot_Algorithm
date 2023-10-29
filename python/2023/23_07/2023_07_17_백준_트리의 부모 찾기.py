# https://www.acmicpc.net/problem/11725

def dfs_stack(start):
    stack = []
    stack.append(start)
    visited[start] = 1
    while stack:
        cur_node = stack.pop()
        for n_node in graph[cur_node]:
            if visited[n_node] == 0:
                result[n_node] = cur_node
                visited[n_node] = 1
                stack.append(n_node)


def dfs_recursion(start):
    visited[start] = 1
    for n_node in graph[start]:
        if visited[n_node] == 0:
            visited[n_node] = 1
            result[n_node] = start
            dfs_recursion(n_node)


def bfs(start):
    from collections import deque
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        cur_node = queue.popleft()
        for n_node in graph[cur_node]:
            if visited[n_node] == 0:
                visited[n_node] = 1
                result[n_node] = cur_node
                queue.append(n_node)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(1000000)
    from collections import defaultdict
    input = sys.stdin.readline

    n = int(input())
    graph = defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (n + 1)
    result = [0] * (n + 1)
    # bfs(1)
    # dfs_stack(1)
    dfs_recursion(1)

    for i in range(2, n+1):
        print(result[i])
