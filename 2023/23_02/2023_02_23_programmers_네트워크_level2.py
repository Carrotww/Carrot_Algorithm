# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    from collections import defaultdict
    result = 0
    stack = []
    visited = [0 for _ in range(n)]
    path = defaultdict(list)
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                path[i].append(j)
    
    for i in range(n):
        if visited[i] == 1:
            continue
        stack.append(i)
        while stack:
            node = stack.pop()
            for n_node in path[node]:
                if visited[n_node] == 1:
                    continue
                stack.append(n_node)
                visited[n_node] = 1
        result += 1
    
    return result