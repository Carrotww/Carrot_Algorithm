# https://www.acmicpc.net/problem/2933

def check(start, end, direct, map, height):
    for i in range(start, direct, end):
        if map[height][i] == 'x':
            return i
    
    return -1

def solve():
    import sys
    row, col = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(row):
        graph.append(list(sys.stdin.readline().strip()))
    N = int(sys.stdin.readline())
    height_list = [0]
    for val in list(map(int, sys.stdin.readline().split())):
        height_list.append(val)
    
    for i in range(1, N):
        cur_height = height_list[i]
        if i % 2 != 0:
            crash_point = check(0, col, 1, graph, cur_height)
        else:
            crash_point = check(col, 0, -1, graph, cur_height)
        if crash_point == -1:
            continue
        


if __name__ == "__main__":
    solve()