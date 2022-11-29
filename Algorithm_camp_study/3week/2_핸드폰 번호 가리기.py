# https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    return '{0}{1}'.format((len(phone_number[:-4]) * '*'), phone_number[-4::])