# https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    temp = [x for x in str(n)]
    return int(''.join(sorted(temp, reverse=True)))