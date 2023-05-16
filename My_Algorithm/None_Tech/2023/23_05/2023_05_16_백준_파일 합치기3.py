# https://www.acmicpc.net/problem/13975

def solve():
    import sys
    import heapq

    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        heap = list(map(int, sys.stdin.readline().split()))
        heapq.heapify(heap)
        result_cnt = 0

        while len(heap) > 1:
            t1 = heapq.heappop(heap)
            t2 = heapq.heappop(heap)

            t_sum = t1 + t2
            result_cnt += t_sum

            heapq.heappush(heap, t_sum)
        print(result_cnt)


if __name__ == "__main__":
    solve()