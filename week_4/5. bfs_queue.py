from collections import deque

graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):
    queue = deque([start_node])
    visited = []
    while queue:
        temp = queue.popleft()
        visited.append(temp)
        for ad in adj_graph[temp]:
            if ad not in visited:
                queue.append(ad)
    return visited


print(bfs_queue(graph, 1))  # 1
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력