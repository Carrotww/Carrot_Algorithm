# https://www.acmicpc.net/problem/2252

if __name__ == "__main__":
    from collections import deque
    import sys
    input = sys.stdin.readline

    graph = dict()
    topology = dict()

    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in topology:
            topology[b] += 1
        else:
            topology[b] = 1

    queue = deque()
    for i in range(1, n+1):
        if i not in topology:
            queue.append(i)

    result = []
    while queue:
        cur_node = queue.popleft()
        result.append(cur_node)
        
        if cur_node in graph:
            for i in graph[cur_node]:
                topology[i] -= 1
                if topology[i] == 0:
                    queue.append(i)
            graph[cur_node] = []
    print(' '.join([str(x) for x in result]))

