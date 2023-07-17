# https://www.acmicpc.net/problem/11000

def solve():
    import sys
    import heapq
    N = int(sys.stdin.readline())

    lecture = []
    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        lecture.append([start, end])

    lecture.sort()
    heap = [lecture[0][1]]

    for i in range(1, N):
        lecture_start_time, lecture_end_time = lecture[i][0], lecture[i][1]
        if lecture_start_time < heap[0]:
            heapq.heappush(heap, lecture_end_time)
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, lecture_end_time)

    print(len(heap))


if __name__ == "__main__":
    solve()
