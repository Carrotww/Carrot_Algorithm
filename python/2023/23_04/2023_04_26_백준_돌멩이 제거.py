# https://www.acmicpc.net/problem/1867

# 최대 이분 매칭
# 최소 버텍스 커버
# 콰니그의 정리

if __name__ == "__main__":
    import sys
    N, K = map(int, sys.stdin.readline().split())
    graph = {x:[] for x in range(1, N+1)}
    for _ in range(K):
        row, col = map(int, sys.stdin.readline().split())
        graph[row].append(col)

    matching = [False for _ in range(N+1)]
    
    def dfs(idx):
        if visited[idx]:
            return False
        visited[idx] = True
        
        for i in graph[idx]:
            idx_i = matching[i]
            if idx_i == False or dfs(idx_i) == True:
                matching[i] = idx
                return True
        return False
    
    result = 0
    for i in range(1, N+1):
        visited = [False for _ in range(N+1)]
        if dfs(i):
            result += 1
    
    print(result)