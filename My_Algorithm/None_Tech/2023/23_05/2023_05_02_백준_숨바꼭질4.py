# https://www.acmicpc.net/problem/13913

def solve():
    import sys
    import heapq
    from collections import deque
    
    N, K = map(int, sys.stdin.readline().split())
    path = [-1] * 100001

    heap = []
    heapq.heappush(heap, [0, N])
    while heap:
        cur_time, cur_node = heapq.heappop(heap)
        for i in [cur_node+1, cur_node-1, cur_node*2]:
            if i < 0 or i > 100000:
                pass