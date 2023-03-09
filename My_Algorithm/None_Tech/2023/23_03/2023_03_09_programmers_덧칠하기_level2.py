# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    cnt = 0
    paint_range = 0
    for sec in section:
        if paint_range == 0:
            paint_range = sec + m - 1
            cnt += 1
        else:
            if paint_range >= sec:
                continue
            else:
                paint_range = sec + m - 1
                cnt += 1
    return cnt