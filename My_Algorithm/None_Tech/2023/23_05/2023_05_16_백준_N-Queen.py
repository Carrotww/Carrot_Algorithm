# https://www.acmicpc.net/problem/9663

import sys
n = int(sys.stdin.readline())
answer = 0
rows = [0] * n

def check(r):
    for i in range(r):
        if rows[i] == rows[r]:
            return False
        if abs(r - i) == abs(rows[r] - rows[i]):
            return False
    return True


def dfs(r):
    global answer
    if r == n:
        answer += 1
        return

    for i in range(n):
        rows[r] = i
        if check(r):
            dfs(r + 1)


dfs(0)
print(answer)
