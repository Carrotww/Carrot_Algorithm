# https://www.acmicpc.net/problem/1629

import sys

def dfs(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return dfs(a, b//2, c) ** 2 % c
    else:
        return dfs(a, b//2, c) ** 2 * a % c

if __name__ == "__main__":
    a, b, c = map(int, sys.stdin.readline().split())

    result = dfs(a, b, c)
    print(result)