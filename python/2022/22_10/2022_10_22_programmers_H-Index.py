# https://school.programmers.co.kr/learn/courses/30/lessons/42747

"""
def solution(citations):
    citations.sort()
    
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    return 0
"""

def solution(citations):
    citations.sort()
    
    for num, val in enumerate(citations):
        if val >= len(citations) - num:
            return len(citations) - num
    return 0