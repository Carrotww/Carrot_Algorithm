# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    cnt, visited = 0, []

    def dfs(index):
        visited.append(index)
        for i in range(n):
            if computers[index][i] == 1 and i not in visited:
                dfs(i)
    
    for i in range(n):
        if i not in visited:
            dfs(i)
            cnt += 1
    
    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))