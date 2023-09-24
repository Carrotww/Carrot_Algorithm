# https://www.acmicpc.net/problem/12100

def find_max_val(graph):
    max_val = 0
    for r in range(N):
        for c in range(N):
            if graph[r][c] > max_val:
                max_val = graph[r][c]
    return max_val

def move(direct, graph):
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    if direct == 0:
        # up
        for c in range(N):
            cur_list = [graph[r][c] for r in range(N)]
            visited = [0] * N
            for i in range(1, N):
                for j in range(0, i):
                    if cur_list[i] == cur_list[j] and visited[i] == 0:
                        visited[i] = 1
                        cur_list[i] *= 2
                        cur_list[j] = 0
                        break
                    elif cur_list[i] == 0:
                        cur_list[i], cur_list[j] = cur_list[j], cur_list[j]
                        break
            for r in range(N):
                graph[r][c] = cur_list[r]
    elif direct == 1:
        # down
        for c in range(N):
            cur_list = [graph[r][c] for r in range(N - 1, -1, -1)]
            visited = [0] * N
            for i in range(1, N):
                for j in range(0, i):
                    if cur_list[i] == cur_list[j] and visited[i] == 0:
                        visited[i] = 1
                        cur_list[i] *= 2
                        cur_list[j] = 0
                        break
                    elif cur_list[i] == 0:
                        cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
                        break
            for r in range(N - 1, -1, -1):
                graph[r][c] = cur_list[r]
    elif direct == 2:
        # left
        for r in range(N):
            cur_list = graph[r]
            visited = [0] * N
            for i in range(1, N):
                for j in range(0, i):
                    if cur_list[i] == cur_list[j] and visited[i] == 0:
                        visited[i] = 1
                        cur_list[i] *= 2
                        cur_list[j] = 0
                        break
                    elif cur_list[i] == 0:
                        cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
                        break
            graph[r] = cur_list
    else:
        # right
        for r in range(N):
            cur_list = graph[r][::-1]
            visited = [0] * N
            for i in range(1, N):
                for j in range(0, i):
                    if cur_list[i] == cur_list[j] and visited[i] == 0:
                        visited[i] = 1
                        cur_list[i] *= 2
                        cur_list[j] = 0
                        break
                    elif cur_list[i] == 0:
                        cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
                        break
            graph[r] = cur_list[::-1]
    
    return graph

def dfs(cnt, graph):
    global result
    if cnt == 0:
        result = max(find_max_val(graph), result)
    for d in range(4):
        # move to 4 direct
        cur_graph = move(d, graph)
        if cur_graph != graph:
            dfs(cnt - 1, cur_graph)
        

if __name__ == "__main__":
    import sys, copy
    input = sys.stdin.readline
    
    N = int(input())
    graph = []
    for _ in range(N):
        t = list(map(int, input().split()))
        graph.append(t)
    
    result = 0

    dfs(5, copy.deepcopy(graph))

    print(result)