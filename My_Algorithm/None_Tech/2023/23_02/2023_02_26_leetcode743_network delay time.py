# https://leetcode.com/problems/network-delay-time/
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        import heapq
        result = 0
        path = defaultdict(list)

        for start, end, time in times:
            path[start - 1].append([end - 1, time])
        
        visited = [0 for _ in range(n)]

        queue = []
        queue.append([0, k-1])
        while queue:
            time, node = heapq.heappop(queue)
            if not visited[node]:
                visited[node] += time
                for n_node, n_time in path[node]:
                    total = time + n_time
                    heapq.heappush(queue, [total, n_node])
        
        for i in range(len(visited)):
            if i == k - 1:
                continue
            if visited[i] == 0:
                return -1
            result = max(visited[i], result)

        return result

# bfs
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict, deque
        result = 0
        path = defaultdict(list)

        for start, end, time in times:
            path[start].append([end, time])
        
        visited = [0 for _ in range(n+1)]
        visited[k] = -1

        queue = deque()
        queue.append((k, 0))
        while queue:
            cur_node, cur_time = queue.popleft()
            for n_node, n_time in path[cur_node]:
                if visited[n_node] == 0 or visited[n_node] > cur_time + n_time:
                    visited[n_node] = n_time + cur_time
                    queue.append((n_node, n_time + cur_time))
        
        for i in range(1, n+1):
            if visited[i] == 0:
                return -1
        return max(visited)