# https://leetcode.com/problems/number-of-islands/

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        visited = [[0] * len(grid[0])] * len(grid)
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

        def dfs(x, y):
            if visited[x][y] == 1 or grid[x][y] == '0':
                return 0
            
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                for i in range(4):
                    n_x, n_y = x + dx[i], y + dy[i]
                    if n_x > 0 and n_x < len(grid) and n_y > 0 and n_y < len(grid[0]):
                        if visited[n_x][n_y] == 0 and grid[n_x][n_y] == '1':
                            visited[n_x][n_y] == 1
                            stack.append((n_x, n_y))
            return 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += dfs(i, j)

        return result