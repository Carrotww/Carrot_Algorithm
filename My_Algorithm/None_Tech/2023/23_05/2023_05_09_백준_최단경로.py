# https://www.acmicpc.net/problem/1753

def solve():
    import sys
    # V -> node cnt E -> edge cnt
    V, E = map(int, sys.stdin.readline().split())
    # K -> start node
    K = int(sys.stdin.readline())
    graph = {x:[] for x in range(1, V+1)}

    for _ in range(E):
        start, end, w = map(int, sys.stdin.readline().split())
        graph[start].append([end, w])
    
    print(graph)

if __name__ == "__main__":
    solve()