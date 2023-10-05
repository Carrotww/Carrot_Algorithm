# https://www.acmicpc.net/problem/2638

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = [(1, 1)]
    n_queue = []

    result = -1
    while queue:
        result += 1
        while queue:
            cur_r, cur_c = queue.pop()
            for d in range(4):
                n_r, n_c = cur_r + dr[d], cur_c + dc[d]
                if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= m):
                    continue
                if graph[n_r][n_c] > 0:
                    graph[n_r][n_c] += 1
                    if graph[n_r][n_c] > 2:
                        n_queue.append((n_r, n_c))
                        graph[n_r][n_c] = -1
                elif graph[n_r][n_c] == 0:
                    queue.append((n_r, n_c))
                    graph[n_r][n_c] = -1
        queue, n_queue = n_queue, queue

    print(result)
