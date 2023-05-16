# https://www.acmicpc.net/problem/1927

def solve():
    import sys, heapq

    N = int(sys.stdin.readline())
    result = []
    check_set = set()
    heap = []
    for _ in range(N):
        cur_num = int(sys.stdin.readline())
        if cur_num == 0:
            if not heap:
                result.append(0)
            else:
                result.append(heapq.heappop(heap))
        else:
            heapq.heappush(heap, cur_num)
    
    for val in result:
        print(val)

if __name__ == "__main__":
    solve()