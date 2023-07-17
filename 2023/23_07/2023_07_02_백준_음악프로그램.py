# https://www.acmicpc.net/problem/2623

def solve():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = defaultdict(list)
    indegree = [0] * (n+1)
    for _ in range(m):
        temp = list(map(int, input().split()))[1::]
        for i in range(1, len(temp)):
            graph[temp[i-1]].append(temp[i])
            indegree[temp[i]] += 1

    result = topology_sort(n, graph, indegree)
    if len(result) != n:
        print(0)
        return
    print(' '.join([str(x) for x in result]))


def topology_sort(n, graph, indegree):
    from collections import deque
    result = []
    queue = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        cur_node = queue.popleft()
        result.append(cur_node)
        for n_node in graph[cur_node]:
            indegree[n_node] -= 1
            if indegree[n_node] == 0:
                queue.append(n_node)
    return result


if __name__ == "__main__":
    solve()
