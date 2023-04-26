# https://www.acmicpc.net/problem/3085

if __name__ == "__main__":
    import sys
    from collections import Counter
    N = int(sys.stdin.readline())
    graph = []
    result = 0

    for i in range(N):
        temp = list(sys.stdin.readline().strip())
        graph.append(temp)
    
    def check():
        global result
        for i in range(N):
            cnt = 1
            for j in range(1, N):
                if graph[i][j-1] == graph[i][j]:
                    cnt += 1
                    result = max(result, cnt)
                else:
                    cnt = 1
            
            cnt = 1
            for j in range(1, N):
                if graph[j-1][i] == graph[j][i]:
                    cnt += 1
                    result = max(result, cnt)
                else:
                    cnt = 1
    
    for row in range(N):
        for col in range(N):
            if row < N-1:
                graph[row][col], graph[row+1][col] = graph[row+1][col], graph[row][col]
                check()
                graph[row][col], graph[row+1][col] = graph[row+1][col], graph[row][col]
            if col < N-1:
                graph[row][col], graph[row][col+1] = graph[row][col+1], graph[row][col]
                check()
                graph[row][col], graph[row][col+1] = graph[row][col+1], graph[row][col]
    
    print(result)