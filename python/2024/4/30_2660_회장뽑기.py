# https://www.acmicpc.net/problem/2660

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    graph = [[float('inf')] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
                break

    while 1:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        graph[a][b] = 1
        graph[b][a] = 1

    for node in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][node] + graph[node][b], graph[a][b])

    result = []
    min_val = float('inf')
    for node in range(1, n+1):
        min_val = min(min_val, max(graph[node][1:]))
        result.append([max(graph[node][1:]), node])

    total = 0
    min_node_list = []
    for val, node in result:
        if val == min_val:
            total += 1
            min_node_list.append(str(node))

    print(min_val, total)
    print(' '.join(min_node_list))


