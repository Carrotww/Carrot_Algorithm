# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            return i
    else:
        return i + 1