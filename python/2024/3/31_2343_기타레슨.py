# https://www.acmicpc.net/problem/2343

def check(ary, time, video_cnt):
    can_make = True
    temp_cnt = 1
    temp_time = 0
    for a in ary:
        if a > time:
            return False
        elif temp_time + a <= time:
            temp_time += a
        else:
            temp_time = a
            temp_cnt += 1
    return temp_cnt <= video_cnt

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())

    ary = list(map(int, input().split()))

    # 그리디? 이분탐색? 잘은 모르겠지만 이분탐색으로 한번 시간을 정해서 돌려볼까? 생각해서 이분탐색임을 깨달음
    # 1 ~ 100000 * 100000 를 범위로 두고 블루레이 동영상을 만들 수 있는 하나의 동영상 길이를 목표로 이분탐색

    result = float('inf')
    # 최소 시간 초기화

    start, end = 1, 10000 * 100000

    while start <= end:
        mid = (start + end) // 2
        if check(ary, mid, m):
            result = min(result, mid)
            # mid -> 해당 동영상 길이로 m개의 동영상을 만들 수 있다면 시간을 줄여본다
            end = mid - 1
        else:
            start = mid + 1

    print(result)

