# https://www.acmicpc.net/problem/13549

def solve2():
    # bfs
    import sys
    from collections import deque
    N, K = map(int, sys.stdin.readline().split())
    visited = [-1] * 100001
    visited[N] = 0

    queue = deque()
    queue.append(N)
    while queue:
        cur_po = queue.popleft()
        if cur_po == K:
            print(visited[cur_po])
            break
        for i in range(3):
            if i == 0:
                n_po = cur_po * 2
            elif i == 1:
                n_po = cur_po - 1
            else:
                n_po = cur_po + 1

            if n_po < 0 or n_po >= 100001 or visited[n_po] != -1:
                continue
            if i == 0:
                if n_po != 0:
                    visited[n_po] = visited[cur_po]
                    queue.appendleft(n_po)
            else:
                visited[n_po] = visited[cur_po] + 1
                queue.append(n_po)

def solve():
    # Dj
    import sys
    import heapq

    N, K = map(int, sys.stdin.readline().split())
    visited = [-1] * 100001
    heap = []
    heapq.heappush(heap, [0, N])

    while heap:
        cnt, cur_node = heapq.heappop(heap)
        if cur_node == K:
            print(cnt)
            break
        for i in range(3):
            if i == 0:
                n_cnt = cnt
                n_node = cur_node * 2
            elif i == 1:
                n_cnt = cnt + 1
                n_node = cur_node + 1
            else:
                n_cnt = cnt + 1
                n_node = cur_node - 1
            if n_node < 0 or n_node >= 100001 or visited[n_node] != -1:
                continue
            visited[n_node] = cnt
            heapq.heappush(heap, [n_cnt, n_node])
    
if __name__ == "__main__":
    solve()