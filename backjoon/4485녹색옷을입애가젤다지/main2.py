import sys, heapq

def solve(n):
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    visited = [[float('inf')] * n for _ in range(n)]
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    hq = [[graph[0][0], 0, 0]]
    visited[0][0] = graph[0][0]

    while hq:
        cost, r, c = heapq.heappop(hq)
        if r == n - 1 and c == n - 1:
            break
        for d in range(4):
            n_r = r + dr[d]
            n_c = c + dc[d]
            if (n_r < 0 or n_r >= n or n_c < 0 or n_c >= n):
                continue
            if visited[n_r][n_c] == float('inf'):
                n_cost = graph[n_r][n_c] + cost
                visited[n_r][n_c] = n_cost
                heapq.heappush(hq, [n_cost, n_r, n_c])

    result.append(visited[n-1][n-1])

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline
    result = []

    while True:
        n = int(input())
        if n != 0:
            solve(n)
        else:
            break

    for i in range(len(result)):
        print(f"Problem {i+1}: {result[i]}")
