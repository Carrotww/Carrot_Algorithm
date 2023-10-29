# https://www.acmicpc.net/problem/1939

def solve():
    import sys
    from collections import defaultdict, deque
    n, m = map(int, sys.stdin.readline().split())
    bri_dict = defaultdict(list)
    
    def bfs(weight, bri_dict, a, b, n):
        queue = deque()
        queue.append(a)
        visited = [0] * (n+1)
        visited[a] = 1

        while queue:
            cur_fac = queue.popleft()
            for n_fac, n_wei in bri_dict[cur_fac]:
                if visited[n_fac] == 0 and n_wei >= weight:
                    visited[n_fac] = 1
                    queue.append(n_fac)
        
        if visited[b]:
            return True
        else:
            return False
     
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        bri_dict[a].append([b, c])
        bri_dict[b].append([a, c])
    
    factory1, factory2 = map(int, sys.stdin.readline().split())
    for i in bri_dict:
        bri_dict[i].sort(key=lambda x:x[1], reverse=True)
    
    start, end = 1, 1000000000
    result = 0
    while start <= end:
        mid = (start + end) // 2
        
        if bfs(mid, bri_dict, factory1, factory2, n):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    print(result)

if __name__ == "__main__":
    solve()