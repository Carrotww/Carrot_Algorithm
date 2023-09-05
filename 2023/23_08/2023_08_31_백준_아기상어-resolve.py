# https://www.acmicpc.net/problem/16236

# https://great-park.tistory.com/26

def bfs(shark_size, baby):
    visited = [[-1] * N for _ in range(N)]
    queue = deque([baby])
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    visited[baby[0]][baby[1]] = 0
    while queue:
        cur_r, cur_c = queue.popleft()
        for direct in range(4):
            n_r, n_c = cur_r+dr[direct], cur_c+dc[direct]
            if (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= N) \
                or shark_size < graph[n_r][n_c] or visited[n_r][n_c] != -1:
                continue
            visited[n_r][n_c] = visited[cur_r][cur_c] + 1
            queue.append([n_r, n_c])

    return visited


def find_fish(visited):
    r, c = 0, 0
    min_distance = float('inf')
    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1 and graph[i][j] != 0 and graph[i][j] < shark_size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    r, c = i, j
    if min_distance == float('inf'):
        return False
    else:
        return r, c, min_distance


if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    N = int(input())
    graph = []
    baby = []
    shark_size = 2
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            if temp[j] == 9:
                baby = [i, j]
        graph.append(temp)
    graph[baby[0]][baby[1]] = 0

    answer = 0
    food = 0

    while 1:
        visited = bfs(shark_size, baby)
        result = find_fish(visited)
        if not result:
            print(answer)
            break
        else:
            baby = [result[0], result[1]]
            answer += result[2]
            graph[result[0]][result[1]] = 0
            food += 1
        if food >= shark_size:
            shark_size += 1
            food = 0
