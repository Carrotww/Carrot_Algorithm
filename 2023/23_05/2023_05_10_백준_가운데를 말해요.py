# https://www.acmicpc.net/problem/1655

def solve():
    import sys
    import heapq
    
    N = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    
    for _ in range(N):
        cur_value = int(sys.stdin.readline())
        
        if not max_heap or (cur_value < -max_heap[0]):
            heapq.heappush(max_heap, -cur_value)
        else:
            heapq.heappush(min_heap, cur_value)
        
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        print(-max_heap[0])

if __name__ == "__main__":
    solve()