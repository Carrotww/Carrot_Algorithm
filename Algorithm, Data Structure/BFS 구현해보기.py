from collections import deque

def dfs(map, start):
    visited = []
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    queue = deque()

    while queue:
        val = queue.popleft()
        if val not in visited:
            visited.append(val)
            for i in map[val]:
                queue.append(i)

    return visited