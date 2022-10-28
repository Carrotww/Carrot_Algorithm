# https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import defaultdict

def solution(participant, completion):
    temp = defaultdict(int)
    for pa in participant:
        temp[pa] += 1
    for com in completion:
        temp[com] -= 1
    for key, val in temp.items():
        if val != 0:
            return key