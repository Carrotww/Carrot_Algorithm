# https://www.acmicpc.net/problem/2693

if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())

    for _ in range(n):
        array = list(map(int, sys.stdin.readline().split()))
        array.sort()
        print(array[-3])