# https://www.acmicpc.net/problem/15683

def solve():
    import sys
    
    N, M = map(int, sys.stdin.readline().split())
    graph = []
    
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    print(graph)

if __name__ == "__main__":
    solve()