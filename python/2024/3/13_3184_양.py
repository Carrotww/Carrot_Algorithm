# https://www.acmicpc.net/problem/3184

def bfs(i, j):
    global result
    o_cnt, v_cnt = 0, 0
    queue = deque([[i, j]])
    visited[i][j] = 1
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    if graph[i][j] == 'v':
        v_cnt += 1
    elif graph[i][j] == 'o':
        o_cnt += 1

    while queue:
        cur_r, cur_c = queue.popleft()
        for d in range(4):
            n_r, n_c = cur_r+dr[d], cur_c+dc[d]
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c) or graph[n_r][n_c] == '#' or visited[n_r][n_c]:
                continue
            if graph[n_r][n_c] == 'v':
                v_cnt += 1
            elif graph[n_r][n_c] == 'o':
                o_cnt += 1
            visited[n_r][n_c] = 1
            queue.append([n_r, n_c])

    if v_cnt + o_cnt > 0 and v_cnt >= o_cnt:
        result[1] += v_cnt
    elif o_cnt > v_cnt:
        result[0] += o_cnt

    
if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    r, c = map(int, input().split())
    graph = []
    for _ in range(r):
        graph.append(list(input().rstrip()))

    visited = [[0] * c for _ in range(r)]
    result = [0, 0]
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and graph[i][j] != '#':
                bfs(i, j)

    print(' '.join([str(x) for x in result]))

'''
문제를 보자마자 bfs를 떠올림.
각 각의 영역을 확인하면서 bfs로 양과 늑대의 개수를 체크하고 결과에 더해주면 됨

놓쳤던 부분 :
1. bfs를 들어가면서 해당 부분 graph[i][j] 가 울타리가 아닐때 함수를 실행시켰는데
양, 늑대일때 bfs 내부에서 양, 늑대 개수를 초기화 시키지 않아서 틀렸었읍
-> 금방 찾았음
'''

