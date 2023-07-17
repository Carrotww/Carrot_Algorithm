# https://www.acmicpc.net/problem/10815

def solve():
    import sys
    N = int(sys.stdin.readline())
    origin_card = list(map(int, sys.stdin.readline().split()))
    origin_card_set = set(origin_card)
    M = int(sys.stdin.readline())
    check_card = list(map(int, sys.stdin.readline().split()))

    result = []

    for cur_num in check_card:
        if cur_num in origin_card_set:
            result.append(1)
        else:
            result.append(0)
    
    print(' '.join([str(x) for x in result]))

if __name__ == "__main__":
    solve()