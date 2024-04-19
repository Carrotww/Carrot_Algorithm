# https://www.acmicpc.net/problem/21278

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        graph[i][i] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

    result = float('inf')
    a_building, b_building = -1, -1
    for i in range(1, n):
        for j in range(i+1, n+1):
            cur_total = 0
            for node in range(1, n+1):
                cur_total += min(graph[i][node]*2, graph[j][node]*2)
            if cur_total < result:
                result = cur_total
                a_building, b_building = i, j
    print(a_building, b_building, result)

