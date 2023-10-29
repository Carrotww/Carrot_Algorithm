# https://leetcode.com/problems/reconstruct-itinerary/

# 첫 번째 풀이
from typing import List

# 타임 오버
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        visited = [0 for _ in range(len(tickets))]
        tickets.sort()

        def dfs(path, visit):
            if len(path) == len(tickets) + 1:
                result.append(path[:])
            for index, val in enumerate(tickets):
                if val[0] == path[-1] and visit[index] == 0:
                    path.append(val[1])
                    visit[index] = 1
                    dfs(path, visit[:])
                    path.pop()
                    visit[index] = 0
        dfs(["JFK"], visited)
        result.sort()

        return result[0]

# 스택 풀이
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        graph = defaultdict(list)
        tickets.sort(reverse=True)
        for a, b in tickets:
            graph[a].append(b)
        
        result = []
        stack = ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            result.append(stack.pop())
        return result[::-1]

# dfs 풀이
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        graph = defaultdict(list)
        tickets.sort(key=lambda x:x[1], reverse=True)
        for start, end in tickets:
            graph[start].append(end)
        
        result = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            result.append(start)
        dfs("JFK")

        return result[::-1]