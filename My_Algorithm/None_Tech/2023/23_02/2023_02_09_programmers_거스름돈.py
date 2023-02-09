# https://school.programmers.co.kr/learn/courses/30/lessons/12907

# 처음 풀이
def solution(n, money):
    temp = []
    
    def dfs(index, change):
        if n == change:
            temp.append(1)
            return
        if n < change:
            return
        for i in range(index, len(money)):
            dfs(i, change + money[i])
    
    for i in range(len(money)):
        dfs(i, money[i])
    
    return len(temp) % 1000000007