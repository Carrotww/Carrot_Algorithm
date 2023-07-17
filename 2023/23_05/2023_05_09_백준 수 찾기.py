# https://www.acmicpc.net/problem/1920

def solve():
    import sys
    N = int(sys.stdin.readline())
    check_list = list(map(int, sys.stdin.readline().split()))
    check_list.sort()

    # number of numbers to check
    M = int(sys.stdin.readline())
    give_list = list(map(int, sys.stdin.readline().split()))

    for cur_num in give_list:
        left, right = 0, len(check_list)
        while left < right:
            mid = (left + right) // 2
            if check_list[mid] < cur_num:
                left = mid + 1
            else:
                right = mid
        if left >= len(check_list):
            print(0)
            continue
        if check_list[left] == cur_num:
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    solve()