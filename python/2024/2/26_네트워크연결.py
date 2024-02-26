# https://www.acmicpc.net/problem/1922

if __name__ == "__main__":
    import sys
    import heapq
    from collections import defaultdict
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    graph = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    

