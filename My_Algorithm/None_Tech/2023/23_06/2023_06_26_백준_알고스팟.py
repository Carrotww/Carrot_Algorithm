# https://www.acmicpc.net/problem/1261

# BFS 풀이
def solve():
    import sys
    from collections import deque
    input = sys.stdin.readline

    col, row = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(row)]
    
    queue = deque()
    queue.append((0, 0))
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    visited = [[-1] * col for _ in range(row)]
    visited[0][0] = 0

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):
            n_row, n_col = cur_row+dr[i], cur_col+dc[i]
            if (n_row < 0 or n_row >= row) or (n_col < 0 or n_col >= col):
                continue
            if visited[n_row][n_col] == -1:
                if graph[n_row][n_col] == 0:
                    visited[n_row][n_col] = visited[cur_row][cur_col]
                    queue.appendleft((n_row, n_col))
                else:
                    visited[n_row][n_col] = visited[cur_row][cur_col] + 1
                    queue.append((n_row, n_col))
    print(visited[row-1][col-1])

# Dijkstra 풀이
def solve1():
    import sys, heapq
    input = sys.stdin.readline

    col, row = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(row)]

    # wall break, row, col
    heap = [(0, 0, 0)]
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[-1] * col for _ in range(row)]
    visited[0][0] = 1

    while heap:
        cur_break, cur_row, cur_col = heapq.heappop(heap)
        for i in range(4):
            n_row, n_col = cur_row+dr[i], cur_col+dc[i]
            if n_row == row-1 and n_col == col-1:
                print(cur_break)
                return
            if (n_row < 0 or n_row >= row) or (n_col < 0 or n_col >= col) or visited[n_row][n_col] == 1:
                continue
            visited[n_row][n_col] = 1
            if graph[n_row][n_col] == 1:
                heapq.heappush(heap, (cur_break+1, n_row, n_col))
            else:
                heapq.heappush(heap, (cur_break, n_row, n_col))
    print(0)
    
if __name__ == "__main__":
    solve1()
