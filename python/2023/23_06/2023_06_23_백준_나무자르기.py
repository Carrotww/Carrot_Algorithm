# https://www.acmicpc.net/problem/2805

def solve():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())

    tree_list = list(map(int, input().split()))
    start, end = 0, max(tree_list)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0
        for tree in tree_list:
            if tree < mid:
                continue
            total += (tree - mid)
        if total >= M:
            start = mid + 1
            result = max(mid, result)
        else:
            end = mid - 1

    print(result)


if __name__ == "__main__":
    solve()
