# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    score.sort()
    min_score = score[0][1]
    cnt = 1

    for i in range(1, n):
        rank = score[i][1]
        if rank < min_score:
            min_score = rank
            cnt += 1
    print(cnt)
    