# https://www.acmicpc.net/problem/1072

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    total_game, win_game = map(int, input().split())
    init_rate = (win_game * 100) // total_game
    if init_rate >= 99:
        print(-1)
        exit()
    next_rate = init_rate + 1

    left, right = 0, 1000000000
    while left <= right:
        mid = (left + right) // 2
        cur_rate = ((win_game + mid) * 100) // (total_game + mid)
        if cur_rate < next_rate:
            left = mid + 1
        else:
            right = mid - 1
    print(left)
