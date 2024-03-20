# https://www.acmicpc.net/problem/1516

def topologysort():
    from collections import deque
    queue = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        cur_node = queue.popleft()
        for n_node, cost in graph[cur_node]:
            visited[n_node] = max(visited[n_node], visited[cur_node] + cost)
            indegree[n_node] -= 1
            if indegree[n_node] == 0:
                queue.append(n_node)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    indegree = [0] * (n + 1)
    graph = [[] for i in range(n+1)]
    visited = [0] * (n + 1)

    for i in range(1, n+1):
        ary = list(map(int, input().split()))
        if ary[1] == -1:
            visited[i] = ary[0]
            continue
        for j in range(1, len(ary)):
            if ary[j] == -1:
                break
            indegree[i] += 1
            graph[ary[j]].append([i, ary[0]])

    topologysort()
    for i in range(1, n+1):
        print(visited[i])


