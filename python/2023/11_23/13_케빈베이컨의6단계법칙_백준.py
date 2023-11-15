# https://www.acmicpc.net/problem/1389

if __name__ == "__main__":
    import sys
    from collections import deque, defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    result = [0] * (n+1)
    for i in range(1, n+1):
        r = [-1] * (n + 1)
        r[i] = 0
        queue = deque([i])

        while queue:
            node = queue.popleft()
            for n_node in graph[node]:
                if r[n_node] == -1 or r[n_node] > r[node] + 1:
                    r[n_node] = r[node] + 1
                    queue.append(n_node)
        result[i] = sum(r)
    result[0] = float('inf')
    for i in range(1, n+1):
        if result[i] == min(result):
            print(i)
            break
