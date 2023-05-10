# https://www.acmicpc.net/problem/10816

def solve():
    import sys
    from collections import Counter
    N = int(sys.stdin.readline())
    origin_card = list(map(int, sys.stdin.readline().split()))
    origin_card_set = set(origin_card)
    origin_counter = Counter(origin_card)
    M = int(sys.stdin.readline())
    check_card = list(map(int, sys.stdin.readline().split()))

    result = []

    for cur_num in check_card:
        if cur_num in origin_card_set:
            result.append(origin_counter[cur_num])
        else:
            result.append(0)
    
    print(' '.join([str(x) for x in result]))

if __name__ == "__main__":
    solve()