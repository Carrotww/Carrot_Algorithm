# https://www.acmicpc.net/problem/18870

def solve1():
    import sys

    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    result_list = [-1] * N

    num_list = [(idx, num) for idx, num in enumerate(num_list)]
    num_list.sort(key=lambda x: x[1])
    cur_num = -1
    check_set = set()

    for idx, num in num_list:
        if num in check_set:
            result_list[idx] = cur_num
        else:
            check_set.add(num)
            cur_num += 1
            result_list[idx] = cur_num

    print(' '.join(str(x) for x in result_list))

def solve():
    import sys
    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    
    num_dict = {x: idx for idx, x in enumerate(sorted(set(num_list)))}
    result = [num_dict[x] for x in num_list]

    print(' '.join([str(x) for x in result]))

if __name__ == "__main__":
    solve()