# https://www.acmicpc.net/problem/2252

def topological_sort(n, graph, indegree):
    queue = deque()
    for i in range(1, n+1):
        if i not in indegree:
            queue.append(i)

    sorted_nodes = []
    while queue:
        cur_node = queue.popleft()
        sorted_nodes.append(cur_node)

        for adjacent_node in graph.get(cur_node, []):
            indegree[adjacent_node] -= 1
            if indegree[adjacent_node] == 0:
                queue.append(adjacent_node)
    return sorted_nodes

if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph, indegree = {}, {}

    for _ in range(m):
        front, back = map(int, input().split())
        if front in graph:
            graph[front].append(back)
        else:
            graph[front] = [back]

        if back in indegree:
            indegree[back] += 1
        else:
            indegree[back] = 1

    sorted_nodes = topological_sort(n, graph, indegree)
    print(' '.join(map(str, sorted_nodes)))
