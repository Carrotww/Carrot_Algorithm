# https://school.programmers.co.kr/learn/courses/30/lessons/12911?language=python3

def bin(num):
    result = ''
    while num != 1:
        result += str(num % 2)
        num //= 2

    cnt = 1
    for r in result:
        if r == '1':
            cnt += 1

    return cnt

def solution(n):
    answer = 0
    cur_cnt = bin(n)
    while bin(n+1) != cur_cnt:
        n += 1

    return n+1

