# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    start, end, i, result = -1, 0, 0, 0
    heap = list()
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(heap, [job[1], job[0]])
        
        if 0 < len(heap):
            temp = heapq.heappop(heap)
            start = end
            end += temp[0]
            result += end - temp[1]
            i += 1
        else:
            end += 1
            
    return result // len(jobs)