# https://www.acmicpc.net/problem/2606

def solve():
    import sys
    from collections import defaultdict, deque

    N = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    graph = defaultdict(list)

    for _ in range(E):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)

    visited = [0] * (N + 1)
    visited[1] = 1
    queue = deque()
    queue.append(1)
    result = 0

    while queue:
        cur_node = queue.popleft()
        for n_node in graph[cur_node]:
            if visited[n_node] == 1:
                continue
            visited[n_node] = 1
            queue.append(n_node)
            result += 1

    print(result)

if __name__ == "__main__":
    solve()