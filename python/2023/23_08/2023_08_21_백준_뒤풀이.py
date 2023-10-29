# https://www.acmicpc.net/problem/14575

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    N, T = map(int, input().split())
    participants = []
    max_l, max_r = -1, -1
    total_l, total_r = 0, 0

    for _ in range(N):
        l, r = map(int, input().split())
        total_l += l
        total_r += r
        participants.append([l, r, r-l])
        max_l = max(max_l, l)
        max_r = max(max_r, r)

    result = float('inf')

    if total_l > T or total_r < T:
        print(-1)
    else:
        l, r = max_l, max_r
        while l <= r:
            mid = (l + r) // 2

            more = 0
            min_sum = 0
            for Li, Ri, diff in participants:
                if Li > mid:
                    break
                more += min(mid, Ri) - Li
                min_sum += Li
            
            if more >= T - min_sum:
                result = mid
                r = mid - 1
            else:
                l = mid + 1

    print(result)

