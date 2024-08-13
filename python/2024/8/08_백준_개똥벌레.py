# https://www.acmicpc.net/problem/3020

# 구해야 하는 것 이분 탐색으로 지나갈때 파괴해야하는 장애물의 최솟값, 해당 최솟값 구간의 개수

def lower_bound(ary, target):
    left, right = 0, len(ary)

    while left < right:
        mid = (left + right) // 2

        if target <= ary[mid]:
            right = mid
        else:
            left = mid + 1

    return right

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, h = map(int, input().split())

    ary = []
    top, bot = [], []

    for _ in range(n // 2):
        bot.append(int(input()))
        top.append(int(input()))

    top.sort()
    bot.sort()

    cave = [0] * h

    for i in range(h):
        cave[i] = n // 2 - lower_bound(top, i + 1) + n // 2 - lower_bound(bot, h - i)

    print(min(cave), cave.count(min(cave)))


