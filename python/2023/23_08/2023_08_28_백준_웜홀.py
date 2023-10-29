# https://www.acmicpc.net/problem/1865

def solve():
    from collections import defaultdict

    N, M, W = map(int, input().split())
    graph = defaultdict(list)
    holl = defaultdict(list)

    for _ in range(M):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
    for _ in range(W):
        s, e, t = map(int, input().split())
        holl[s].append([e, t])
    
    # 1 3 4
    # 3 1 3

    # for i in range(holl):
    #     print(holl[i])
    #     e = holl[i][0]
    #     minus_t = holl[i][1]

    #     if graph[e]:
    #         for s, t in graph[e]:
    #             if s == i and minus_t > t:
    #                 print('YES')
    #                 return

    print(holl[3])
    print('NO')
    

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    TC = int(input())
    for _ in range(TC):
        solve()