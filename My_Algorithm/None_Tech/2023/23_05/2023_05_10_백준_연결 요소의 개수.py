# https://www.acmicpc.net/problem/11724

def solve():
    import sys
    from collections import defaultdict, deque

    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)
    
    visited = [0] * (N+1)
    result_cnt = 0
    
    for idx in range(1, N+1):
        if visited[idx] == 0:
            visited[idx] = 1
            result_cnt += 1
            stack = [idx]
            while stack:
                cur_node = stack.pop()
                for n_node in graph[cur_node]:
                    if visited[n_node] == 0:
                        visited[n_node] = 1
                        stack.append(n_node)
    
    print(result_cnt)
    

if __name__ == "__main__":
    solve()