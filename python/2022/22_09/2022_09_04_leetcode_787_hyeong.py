# https://leetcode.com/problems/cheapest-flights-within-k-stops/

import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight = [[] for _ in range(n)]
        for a, b, c in flights:
            flight[a].append((b, c))
        pq = []
        cnt = 0
        pq.append((0, src, cnt))
        visit = dict()

        while pq:
            intensity, node, cnt = heapq.heappop(pq)
            if node == dst:
                return intensity
            if node not in visit or cnt <= visit[node]:
                visit[node] = cnt
                for next_node, next_val in flight[node]:
                    if cnt > k:
                        continue
                    heapq.heappush(pq, (intensity + next_val, next_node, cnt + 1))

        return -1

example = Solution()
print(example.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))