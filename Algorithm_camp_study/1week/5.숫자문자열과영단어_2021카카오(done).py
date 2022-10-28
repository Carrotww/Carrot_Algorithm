# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for num, val in enumerate(word_list):
        s = s.replace(val, str(num))
    
    return int(s)