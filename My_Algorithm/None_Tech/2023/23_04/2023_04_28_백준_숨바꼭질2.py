# https://www.acmicpc.net/problem/12851

def solve():
    import sys
    from collections import deque
    
    N, K = map(int, sys.stdin.readline().split())
    visited = [0] * 100001
    
    def bfs(n, K):
        queue = deque()
        queue.append([n, 0])
        result = 0
        min_cnt = float('inf')
        
        while queue:
            cur_po, cnt = queue.popleft()
            if cur_po == K:
                if cnt < min_cnt:
                    min_cnt = cnt
                    result = 1
                elif cnt == min_cnt:
                    result += 1
                    continue

            for i in [cur_po-1, cur_po+1, cur_po*2]:
                if (i < 0 or i >= 100001) or (visited[i] != 0 and (visited[i] < visited[cur_po]+1)):
                    continue
                visited[i] = visited[cur_po] + 1
                queue.append([i, cnt+1])
        
        return [min_cnt, result]
    
    a, b = bfs(N, K)
    print(a)
    print(b)

if __name__ == "__main__":
    solve()