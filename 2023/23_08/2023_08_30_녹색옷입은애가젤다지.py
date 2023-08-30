# https://www.acmicpc.net/problem/4485

def solve(n):
    heap = []
    graph = []
    for _ in range(n):
        t = list(map(int, input().split()))
        graph.append(t)
    
    heap.append([graph[0][0], 0, 0])
    result = 0
    visited = [[0] * n for _ in range(n)]
    while heap:
        cur_t, cur_r, cur_c = heapq.heappop(heap)
        for direct in range(4):
            n_r, n_c = cur_r+dr[direct], cur_c+dc[direct]
            if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= n) or visited[n_r][n_c] == 1:
                continue
            if n_r == n-1 and n_c == n-1:
                result = graph[n_r][n_c] + cur_t
                return result
            else:
                heapq.heappush(heap, [cur_t+graph[n_r][n_c], n_r, n_c])
                visited[n_r][n_c] = 1

if __name__ == "__main__":
    import sys, heapq
    input = sys.stdin.readline
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    cnt = 1
    
    while 1:
        N = int(input())
        if N != 0:
            result = solve(N)
            print(f"Problem {cnt}: {result}")
            cnt += 1
        else:
            break