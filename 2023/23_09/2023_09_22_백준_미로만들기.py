# https://www.acmicpc.net/problem/2665

if __name__ == "__main__":
    import sys
    import heapq

    input = sys.stdin.readline

    n = int(input())
    graph = []
    for _ in range(n):
        temp = list(map(int, input().rstrip()))
        graph.append(temp)

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    # break wall cnt, row, col
    heap = [(0, 0, 0)]
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0
    result = 0

    while heap:
        cur_break, cur_r, cur_c = heapq.heappop(heap)
        if cur_r == n - 1 and cur_c == n - 1:
            result = cur_break
            break
        for d in range(4):
            n_r, n_c = cur_r+dr[d], cur_c+dc[d]
            if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= n):
                continue
            n_break = cur_break
            if graph[n_r][n_c] == 0: n_break += 1
            if visited[n_r][n_c] == -1 or visited[n_r][n_c] > n_break:
                visited[n_r][n_c] = n_break
                heapq.heappush(heap, (n_break, n_r, n_c))

    print(result)