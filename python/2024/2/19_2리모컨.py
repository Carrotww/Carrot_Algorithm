# https://www.acmicpc.net/problem/1107

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    start = 100
    target = input()
    broken_cnt = int(input())
    broken_btn = list()
    if broken_cnt > 0:
        broken_btn = input().split()

    press_cnt = abs(int(target) - start)
    result = press_cnt
    for i in range(1000000):
        for cur_num in str(i):
            if cur_num in broken_btn:
                break
        else:
            result = min(result, abs(int(target) - i) + len(str(i)))

    print(result)

