# https://www.acmicpc.net/problem/9934

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    k = int(input())
    visited = list(map(int, input().split()))

    graph = [[] for _ in range(k)]
    def mid(start, end, depth):
        if start == end:
            graph[depth].append(visited[start])
            return
        root = (start + end) // 2
        graph[depth].append(visited[root])
        mid(start, root-1, depth+1)
        mid(root+1, end, depth+1)
    
    mid(0, len(visited)-1, 0)

    for i in graph:
        print(' '.join([str(x) for x in i]))

