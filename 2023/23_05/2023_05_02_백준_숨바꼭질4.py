# https://www.acmicpc.net/problem/13913

def solve():
    import sys
    import heapq
    
    N, K = map(int, sys.stdin.readline().split())
    path = [-1] * 100001
    visited = [-1] * 100001

    heap = []
    result_time = 0
    heapq.heappush(heap, [0, N])
    while heap:
        cur_time, cur_node = heapq.heappop(heap)
        if cur_node == K:
            result_time = cur_time
            break
            
        for n_node in [cur_node+1, cur_node-1, cur_node*2]:
            if n_node < 0 or n_node > 100000 or visited[n_node] != -1:
                continue
            visited[n_node] = cur_time + 1
            path[n_node] = cur_node
            heapq.heappush(heap, [cur_time+1, n_node])
    
    print(result_time)
    
    result_path = []
    start, end = N, K
    result_path.append(end)
    while start != end:
        result_path.append(path[end])
        end = path[end]
    print(' '.join([str(x) for x in result_path[::-1]]))

if __name__ == "__main__":
    solve()