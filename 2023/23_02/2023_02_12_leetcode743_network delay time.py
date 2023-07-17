# https://leetcode.com/problems/network-delay-time/

from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        import heapq

        path = defaultdict(list)
        dist = defaultdict(list)
        
        for start, end, time in times:
            path[start].append([end, time])
        
        queue = [[0, k]]

        while queue:
            time, node = heapq.heappop(queue)
            if node not in dist:
                dist[node] = time
                for n_node, n_time in path[node]:
                    heapq.heappush(queue, [time + n_time, n_node])
        
        if len(dist) == n:
            return max(dist.values())
        
        return -1