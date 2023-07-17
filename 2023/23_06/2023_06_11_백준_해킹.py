# https://www.acmicpc.net/problem/10282

def solve():
    import sys, heapq
    from collections import defaultdict
    n, d, c = map(int, sys.stdin.readline().split())
    dpcy = defaultdict(list)
    visited = [float('inf')] * (n+1)
    for _ in range(d):
        a, b, t = map(int, sys.stdin.readline().split())
        dpcy[b].append([a, t])
    heap = []
    heap.append([0, c])
    visited[c] = 0
    cnt, result = 0, 0
    
    while heap:
        time, node = heapq.heappop(heap)
        for nnode, ttime in dpcy[node]:
            if visited[nnode] > ttime + time:
                visited[nnode] = ttime + time
                heapq.heappush(heap, [ttime + time, nnode])
    
    temp = [x for x in visited if x != float('inf')]
    cnt, result = len(temp), max(temp)
    
    return cnt, result

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline())
    for _ in range(N):
        a, b = solve()
        print(f'{a} {b}')