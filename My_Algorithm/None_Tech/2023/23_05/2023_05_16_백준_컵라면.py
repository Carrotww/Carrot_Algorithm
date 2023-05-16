# https://www.acmicpc.net/problem/1781

def solve():
    import sys, heapq

    N = int(sys.stdin.readline())
    problem_list = []

    for _ in range(N):
        dead, cup = map(int, sys.stdin.readline().split())
        problem_list.append([dead, cup])
    
    problem_list.sort()
    
    heap = []
    
    for dead, cup in problem_list:
        heapq.heappush(heap, cup)

        if len(heap) > dead:
            heapq.heappop(heap)
    
    print(sum(heap))

if __name__ == "__main__":
    solve()