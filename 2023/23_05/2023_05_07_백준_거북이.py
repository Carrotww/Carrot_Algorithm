# https://www.acmicpc.net/problem/8911

def solve(graph):
    cur_r, cur_c = 0, 0
    path = [[cur_r, cur_c]]

    direct = 0
    # idx : 0 -> 위를 보고 있음, idx : 1 -> 오른쪽, idx : 2 -> 아래, idx : 3 -> 왼쪽
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    for i in graph:
        if i == 'F':
            cur_r, cur_c = cur_r+dr[direct], cur_c+dc[direct]
            path.append([cur_r, cur_c])
        elif i == 'B':
            cur_r, cur_c = cur_r-dr[direct], cur_c-dc[direct]
            path.append([cur_r, cur_c])
        elif i == 'L':
            direct -= 1
            if direct < -4:
                direct = -1
        elif i == 'R':
            direct += 1
            if direct > 3:
                direct = 0
    
    min_r, max_r, min_c, max_c = float('inf'), 0, float('inf'), 0

    for pa in path:
        r, c = pa
        min_r = min(r, min_r)
        max_r = max(r, max_r)
        min_c = min(c, min_c)
        max_c = max(c, max_c)
    
    result = (abs(min_r) + max_r) * (abs(min_c) + max_c)
    print(result)
    
if __name__ == "__main__":
    import sys
    for _ in range(int(sys.stdin.readline())):
        temp = sys.stdin.readline().strip()
        solve(temp)