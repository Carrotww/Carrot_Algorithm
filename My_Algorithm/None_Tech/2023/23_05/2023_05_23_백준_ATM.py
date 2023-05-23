# https://www.acmicpc.net/problem/11399

def solve():
    import sys
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    a.sort()

    result = 0
    temp = 0
    for i in a:
        temp += i
        result += temp

    print(result)


if __name__ == "__main__":
    solve()