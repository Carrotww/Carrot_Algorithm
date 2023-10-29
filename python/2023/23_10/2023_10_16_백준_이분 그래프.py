# https://www.acmicpc.net/problem/1707

def dfs(node, color):
    visited[node] = color
    for n_node in graph[node]:
        if visited[n_node] == 0:
            if not dfs(n_node, -color):
                return False
        elif visited[n_node] == color:
            return False

    return True


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(100000)

    k = int(input())
    for _ in range(k):
        v, e = map(int, input().split())
        graph = [[] for _ in range(v+1)]
        for _ in range(e):
            start, end = map(int, input().split())
            graph[start].append(end)
            graph[end].append(start)

        visited = [0] * (v + 1)
        is_true = True
        for node in range(1, v+1):
            if visited[node] == 0:
                is_true = dfs(node, 1)
                if is_true == False:
                    break
                    
        if is_true:
            print("YES")
        else:
            print("NO")