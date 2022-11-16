graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []
    while stack:
        temp = stack.pop()
        visited.append(temp)
        for ad in adjacent_graph[temp]:
            if ad not in visited:
                stack.append(ad)

    return visited


print(dfs_stack(graph, 1))  # 1
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4]