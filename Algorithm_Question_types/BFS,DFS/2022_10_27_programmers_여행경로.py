# https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict

def solution(tickets):
    visited, path, stack = [], ["ICN"], ["ICN"]
    tic = defaultdict(list)
    for a, b in tickets:
        tic[a].append(b)
    for t in tic.values():
        t.sort()
    
    def dfs(visited, path, stack):
        # if not stack:
        #     return path
        start = stack.pop()
        if start in tic:
            for i in tic[start]:
                if (start, i) not in visited:
                    visited.append((start, i))
                    stack.append(i)
                    path.append(i)
                    dfs(visited, path, stack)
    
    dfs(visited, path, stack)
    
    return path

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))