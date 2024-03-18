# https://www.acmicpc.net/problem/12100

def move(direct, graph):
    if direct == 0:
        for col in range(n):
            position = 0
            for row in range(1, n):
                if graph[row][col] != 0:
                    temp = graph[row][col]
                    graph[row][col] = 0
                    if graph[position][col] == 0:
                        graph[position][col] = temp
                    elif graph[position][col] == temp:
                        graph[position][col] *= 2
                        position += 1
                    else:
                        position += 1
                        graph[position][col] = temp

    elif direct == 1:
        for row in range(n):
            position = n-1
            for col in range(n-2, -1, -1):
                if graph[row][col] != 0:
                    temp = graph[row][col]
                    graph[row][col] = 0
                    if graph[row][position] == 0:
                        graph[row][position] = temp
                    elif graph[row][position] == temp:
                        graph[row][position] *= 2
                        position -= 1
                    else:
                        position -= 1
                        graph[row][position] = temp
    
    elif direct == 2:
        for col in range(n):
            position = n-1
            for row in range(n-2, -1, -1):
                if graph[row][col] != 0:
                    temp = graph[row][col]
                    graph[row][col] = 0
                    if graph[position][col] == 0:
                        graph[position][col] = temp
                    elif graph[position][col] == temp:
                        graph[position][col] *= 2
                        position -= 1
                    else:
                        position -= 1
                        graph[position][col] = temp

    else:
        for row in range(n):
            position = 0
            for col in range(1, n):
                if graph[row][col] != 0:
                    temp = graph[row][col]
                    graph[row][col] = 0
                    if graph[row][position] == 0:
                        graph[row][position] = temp
                    elif graph[row][position] == temp:
                        graph[row][position] *= 2
                        position += 1
                    else:
                        position += 1
                        graph[row][position] = temp

    return graph

def dfs(cnt, graph):
    if cnt == 5:
        return max(map(max, graph))

    max_val = 0
    for d in range(4):
        n_graph = deepcopy(graph)
        n_graph = move(d, n_graph)
        max_val = max(max_val, dfs(cnt+1, n_graph))
    return max_val


if __name__ == "__main__":
    import sys
    from copy import deepcopy
    input = sys.stdin.readline

    n = int(input())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    result = dfs(0, graph)
    print(result)

