# https://www.acmicpc.net/problem/1389

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = dict()
    for _ in range(n):
        start, end = map(int, input().split())
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
        if end in graph:
            graph[end].append(start)
        else:
            graph[end] = [start]

