# https://www.acmicpc.net/problem/1477

def solve():
    import sys, heapq
    input = sys.stdin.readline
    
    n, m, l = map(int, input().split())
    station = list(map(int, input().split()))
    station.append(l)
    station.sort()
    heap = []
    for i in range(1, n+1):
        station_range = station[i] - station[i-1]
        heapq.heappush(heap, -station_range)
    
    for _ in range(m):
        cur_num = -heapq.heappop(heap)
        temp = cur_num // 2
        temp2 = cur_num - temp
        heapq.heappush(heap, -temp)
        heapq.heappush(heap, -temp2)
    
    print(-heapq.heappop(heap))

if __name__ == "__main__":
    solve()