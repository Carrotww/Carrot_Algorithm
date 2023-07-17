# https://www.acmicpc.net/problem/11279

def solve():
    import sys, heapq
    input = sys.stdin.readline
    N = int(input())

    heap = []
    result = []

    for _ in range(N):
        command = int(input())
        if command == 0:
            if not heap:
                result.append(0)
            else:
                result.append(-heapq.heappop(heap))
        else:
            heapq.heappush(heap, -command)
    
    for r in result:
        print(r)

if __name__ == "__main__":
    solve()