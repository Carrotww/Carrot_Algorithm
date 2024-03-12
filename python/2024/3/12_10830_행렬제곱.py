# https://www.acmicpc.net/problem/10830

def cal(ary1, ary2):
    n_ary = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            total = 0
            for z in range(n):
                total += ary1[i][z] * ary2[z][j]
            n_ary[i][j] = total % 1000
    return n_ary

def solve(ary, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                ary[i][j] %= 1000
        return ary

    t = solve(ary, b // 2)
    if b % 2 == 0:
        return cal(t, t)
    else:
        return cal(cal(t, t), ary)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    ary = []
    for _ in range(n):
        ary.append(list(map(int, input().split())))

    result = solve(ary, k)
    for i in range(n):
        print(' '.join([str(x) for x in result[i]]))

