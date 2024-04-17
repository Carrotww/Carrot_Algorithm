# https://www.acmicpc.net/problem/14923

if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    r, c = map(int, input().split())
    start_r, start_c = map(int, input().split())
    target_r, target_c = map(int, input().split())

    graph = []
    for _ in range(r):
        graph.append(list(map(int, input().split())))

    visited = [[[0] for _ in range(c)] for _ in range(r)]
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

    queue = deque([(start_r, start_c, 0, 0)])
    while queue:
        cur_r, cur_c, is_broke, cnt = queue.popleft()



