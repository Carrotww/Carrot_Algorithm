# https://www.acmicpc.net/problem/18428

def check():
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    for t_r, t_c in teacher:
        for d in range(4):
            n_r, n_c = t_r+dr[d], t_c+dc[d]
            while 1:
                if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= n) or graph[n_r][n_c] == 'O':
                    break
                elif graph[n_r][n_c] == 'S':
                    return False
                else:
                    n_r, n_c = n_r+dr[d], n_c+dc[d]
    return True


def dfs(num, r, c):
    if num == 3:
        return check()
    else:
        for i in range(r, n):
            start_c = c
            if i > r:
                start_c = 0
            for j in range(start_c, n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    if dfs(num+1, i, j):
                        return True
                    graph[i][j] = 'X'
        return False

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    graph = []
    for _ in range(n):
        t = list(input().split())
        graph.append(t)
    teacher = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'T':
                teacher.append([i, j])

    visited = [[0] * n for _ in range(n)]
    result = dfs(0, 0, 0)
    if result:
        print('YES')
    else:
        print('NO')

