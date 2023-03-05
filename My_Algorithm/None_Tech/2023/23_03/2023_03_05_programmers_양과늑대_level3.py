# https://school.programmers.co.kr/learn/courses/30/lessons/92343

# 첫 번째 풀이 - 못 품
def solution(info, edges):
    from collections import defaultdict
    path = defaultdict(list)
    for start, end in edges:
        path[start].append(end)
        path[end].append(start)
    
    print(path)
    result = 0
    
    visited = [0] * len(info)
    visited[0] = -1
    
    def dfs(node, vs, sheep, wolf):
        for n_node in path[node]:
            if info[node] == 0:
                vs[node] = -1
                sheep += dfs(n_node, vs, sheep + 1, wolf)
            else:
                wolf += 1
                if sheep <= wolf:
                    continue
                vs[node] = -1
                sheep += dfs(n_node, vs, sheep, wolf + 1)
                
        return sheep
    
    result = dfs(0, visited, 1, 0)
    
    return result