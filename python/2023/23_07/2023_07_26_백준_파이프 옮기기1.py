# https://www.acmicpc.net/problem/17070

def bfs():
    from collections import deque
    queue = deque()
    start = (0, 0, 1)
    queue.append(start)
    cnt = 0
    if graph[n-1][n-1] == 1:
        return cnt
    # 0 -> 가로, 1 -> 세로, 2 -> 대각선
    while queue:
        cur_direct, cur_r, cur_c = queue.popleft()
        if cur_r == n-1 and cur_c == n-1:
            cnt += 1
            continue
        if cur_direct == 0:
            for direct, dr, dc in ((0, 0, 1), (2, 1, 1)):
                n_r, n_c = cur_r+dr, cur_c+dc
                if direct == 2:
                    if check(cur_r+1, cur_c) or check(cur_r, cur_c+1) or check(cur_r+1, cur_c+1):
                        continue
                else:
                    if check(n_r, n_c):
                        continue
                queue.append((direct, n_r, n_c))

        elif cur_direct == 1:
            for direct, dr, dc in ((1, 1, 0), (2, 1, 1)):
                n_r, n_c = cur_r+dr, cur_c+dc
                if direct == 2:
                    if check(cur_r+1, cur_c) or check(cur_r, cur_c+1) or check(cur_r+1, cur_c+1):
                        continue
                else:
                    if check(n_r, n_c):
                        continue
                queue.append((direct, n_r, n_c))
        else:
            for direct, dr, dc in ((0, 0, 1), (1, 1, 0), (2, 1, 1)):
                n_r, n_c = cur_r+dr, cur_c+dc
                if direct == 2:
                    if check(cur_r+1, cur_c) or check(cur_r, cur_c+1) or check(cur_r+1, cur_c+1):
                        continue
                else:
                    if check(n_r, n_c):
                        continue
                queue.append((direct, n_r, n_c))

    return cnt


def dfs():
    queue = []
    start = (0, 0, 1)
    queue.append(start)
    cnt = 0
    if graph[n-1][n-1] == 1:
        return cnt
    # 0 -> 가로, 1 -> 세로, 2 -> 대각선
    while queue:
        cur_direct, cur_r, cur_c = queue.pop()
        if cur_r == n-1 and cur_c == n-1:
            cnt += 1
            continue
        if cur_direct == 0:
            for direct, dr, dc in ((0, 0, 1), (2, 1, 1)):
                n_r, n_c = cur_r+dr, cur_c+dc
                if direct == 2:
                    if check(cur_r+1, cur_c) or check(cur_r, cur_c+1) or check(cur_r+1, cur_c+1):
                        continue
                else:
                    if check(n_r, n_c):
                        continue
                queue.append((direct, n_r, n_c))

        elif cur_direct == 1:
            for direct, dr, dc in ((1, 1, 0), (2, 1, 1)):
                n_r, n_c = cur_r+dr, cur_c+dc
                if direct == 2:
                    if check(cur_r+1, cur_c) or check(cur_r, cur_c+1) or check(cur_r+1, cur_c+1):
                        continue
                else:
                    if check(n_r, n_c):
                        continue
                queue.append((direct, n_r, n_c))
        else:
            for direct, dr, dc in ((0, 0, 1), (1, 1, 0), (2, 1, 1)):
                n_r, n_c = cur_r+dr, cur_c+dc
                if direct == 2:
                    if check(cur_r+1, cur_c) or check(cur_r, cur_c+1) or check(cur_r+1, cur_c+1):
                        continue
                else:
                    if check(n_r, n_c):
                        continue
                queue.append((direct, n_r, n_c))

    return cnt


def check(r, c):
    if (r < 0 or r >= n) or (c < 0 or c >= n) or graph[r][c] == 1:
        return True
    return False


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    result_cnt = dfs()
    # result_cnt = bfs()
    print(result_cnt)
