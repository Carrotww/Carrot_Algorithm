# https://www.acmicpc.net/problem/21278

def solve(a, b):
    import heapq
    a_chicken, b_chicken = [0] * (n+1), [0] * (n+1)

    a_visited, b_visited = [0] * (n+1), [0] * (n+1)

if __name__ == "__main__":
    import sys, itertools
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        start, end = map(int, input().split())
        if not graph[start]:
            graph[start] = [end]
        else:
            graph[start].append(end)

        if not graph[end]:
            graph[end] = [start]
        else:
            graph[end].append(start)

    result = float('inf')

    for a, b in itertools.combinations([x for x in range(1, n+1)], 2):
        result = min(result, solve(a, b))

    print(result)


