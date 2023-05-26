# https://www.acmicpc.net/problem/11003

def solve():
    import sys
    import heapq
    from collections import deque

    N, L = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    result = []

    queue = deque()
    min_idx = 0
    for idx in range(len(a)):
        if idx - L + 1 < 0:
            continue
        else:
            min_idx = idx

    min_val = a[0]
    min_val_cnt = 1
    for idx in range(0, min_idx+1):
        cur_val = a[idx]
        if min_val < cur_val:
            result.append(min_val)
        elif min_val == cur_val:
            result.append(min_val)
            min_val_cnt += 1
        else:
            result.append(cur_val)
            min_val_cnt = 1

    for idx in range(min_idx, len(a)):
        cur_val = a[idx]
        pre_val = queue.popleft()
        if min_val == pre_val:
            if min_val_cnt == 1:
                min_val = min(queue)
            else:
                min_val_cnt -= 1

    print(' '.join([str(x) for x in result]))


if __name__ == "__main__":
    solve()
