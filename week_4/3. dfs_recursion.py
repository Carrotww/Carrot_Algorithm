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
visited = []


def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    for ad in adjacent_graph[cur_node]:
        if ad not in visited_array:
            dfs_recursion(adjacent_graph, ad, visited_array)
    return


dfs_recursion(graph, 1, visited)  # 1 이 시작노드
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력