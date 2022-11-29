# https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    result = s.lower()
    if result.count('p') != result.count('y'):
        return False
    return True