# https://www.acmicpc.net/problem/16926

def turn_arr():
    for depth in range(min(n, m) // 2):
        n_max = n - depth - 1
        m_max = m - depth - 1
        
        tmp = graph[depth][depth]
        
        # 윗라인
        for j in range(depth, m_max):
            graph[depth][j] = graph[depth][j + 1]
        
        # 오른쪽
        for j in range(depth, n_max):
            graph[j][m_max] = graph[j+1][m_max]
        
        # 아래
        for j in range(m_max, depth, -1):
            graph[n_max][j] = graph[n_max][j-1]
        
        # 왼쪽
        for j in range(n_max, depth, -1):
            graph[j][depth] = graph[j-1][depth]
        
        graph[depth+1][depth] = tmp

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m, r = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    for _ in range(r):
        turn_arr()
    
    for i in range(n):
        print(' '.join(map(str, graph[i])))