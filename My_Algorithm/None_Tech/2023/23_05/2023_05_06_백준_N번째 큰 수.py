# https://www.acmicpc.net/problem/2693

def solve():
    import sys
    N = int(sys.stdin.readline())

    for _ in range(N):
        cur_list = list(map(int, sys.stdin.readline().split()))
        cur_list.sort()
        print(cur_list[7])

if __name__ == "__main__":
    solve()