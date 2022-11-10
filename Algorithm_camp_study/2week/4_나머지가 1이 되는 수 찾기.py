# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    return [x for x in range(1, n + 1) if n % x == 1][0]