# https://www.acmicpc.net/problem/1700

def solve():
    import sys
    N, K = map(int, sys.stdin.readline().split())
    multitab = []
    use_list = list(map(int, sys.stdin.readline().split()))
    unplugs = 0

    for idx, val in enumerate(use_list):
        if val in multitab:
            continue
        
        if len(multitab) < N:
            multitab.append(val)
        else:
            max_unused_idx = -1
            to_nuplug = -1
            for plug_num in multitab:
                if plug_num not in use_list[idx:][0:K]:
                    to_nuplug = plug_num
                    break
                index = use_list[idx:].index(plug_num)
                if index > max_unused_idx:
                    max_unused_idx = index
                    to_nuplug = plug_num
            unplugs += 1
            multitab.remove(to_nuplug)
            multitab.append(val)
    print(unplugs)
    return

if __name__ == "__main__":
    solve()