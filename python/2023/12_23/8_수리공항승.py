# https://www.acmicpc.net/problem/1449

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, l = map(int, input().split())
    water_position = list(map(int, input().split()))
    water_position.sort(reverse=True)

    result = 1
    cur_len = l - 1
    pre_num = water_position.pop()
    while water_position:
        cur_num = water_position.pop()
        if cur_len - (cur_num - pre_num) >= 0:
            cur_len -= (cur_num - pre_num)
            pre_num = cur_num
        else:
            result += 1
            cur_len = l - 1
            pre_num = cur_num
    print(result)
