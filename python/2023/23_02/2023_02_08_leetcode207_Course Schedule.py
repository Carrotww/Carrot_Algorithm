# https://leetcode.com/problems/course-schedule/description/

from typing import List

class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        from collections import defaultdict

        graph = defaultdict(list)

        for start, end in pre:
            graph[start].append(end)
        
        path, visited = set(), set()

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            for start in graph[node]:
                if not dfs(start):
                    return False
            
            path.remove(node)
            visited.add(node)
            return True
        
        for start in list(graph):
            if not dfs(start):
                return False
        
        return True