# https://www.acmicpc.net/problem/1715

def solve():
    import sys, heapq
    input = sys.stdin.readline
    
    n = int(input())
    heap = []

    for i in range(n):
        cur_num = int(input())
        heap.append(cur_num)
    heapq.heapify(heap)
    
    if n == 1:
        print(0)
        return

    result = 0

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b)
        result += (a+b)

    print(result)

if __name__ == "__main__":
    solve()