# https://www.acmicpc.net/problem/15649

def solve():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    visited = [0 for _ in range(N)]
    value_list = [x for x in range(1, N+1)]
    result = []

    def dfs(cnt, num_list):
        if cnt == M:
            result.append(num_list[:])
            return
        
        for idx, val in enumerate(value_list):
            if visited[idx] == 1:
                continue
            num_list.append(val)
            visited[idx] = 1
            
            dfs(cnt+1, num_list)
            num_list.pop()
            visited[idx] = 0
    
    dfs(0, [])
    for re in result:
        print(' '.join([str(x) for x in re]))

if __name__ == "__main__":
    solve()