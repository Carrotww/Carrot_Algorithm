# https://www.acmicpc.net/problem/17070

if __name__ == "__main__":
    from collections import deque
    import sys
    input = sys.stdin.readline

    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    '''
    horizon = [(0, 1), (1, 1)]
    # 가로 방향 (오른쪽) (오른쪽아래대각선)
    vertical = [(1, 0), (1, 1)]
    # 세로 방향 (아래) (오른쪽아래대각선)
    diag = [(0, 1), (1, 0), (1, 1)]
    # 대각선 방향 (오른쪽) (아래) (오른쪽 아래 대각선)
    '''

    direct = [[(0, 1, 0), (1, 1, 1)], [(0, 1, 0), (1, 0, 2), (1, 1, 1)], [(1, 0, 2), (1, 1, 1)]]

    queue = deque()
    if graph[n-1][n-1] == 0:
        queue.append([0, 1, 0])
    # visited = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    result = 0

    while queue:
        cur_r, cur_c, cur_d = queue.popleft()
        if (cur_r, cur_c) == (n-1, n-1):
            result += 1
            continue
        for r_d, c_d, d in direct[cur_d]:
            n_r, n_c = cur_r+r_d, cur_c+c_d
            if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= n) or graph[n_r][n_c] == 1:
                continue
            if d == 1:
                if (graph[n_r-1][n_c] == 1 or graph[n_r][n_c-1] == 1):
                    continue
            queue.append([n_r, n_c, d])

    print(result)


