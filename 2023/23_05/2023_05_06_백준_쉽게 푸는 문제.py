# https://www.acmicpc.net/problem/1292

def solve():
    import sys
    
    A, B = map(int, sys.stdin.readline().split())

    idx = 1
    cur_num = 1
    cnt_dict = {}
    for i in range(1, 1001):
        cnt_dict[i] = 0
    result = 0
    while idx <= B:
        if A <= idx <= B:
            result += cur_num
        cnt_dict[cur_num] += 1
        if cnt_dict[cur_num] == cur_num:
            cur_num += 1
        idx += 1
    
    print(result)

if __name__ == "__main__":
    solve()