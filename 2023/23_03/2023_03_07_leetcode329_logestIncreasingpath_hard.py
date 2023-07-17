# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

from typing import List
# 풀이 - dp - 상위 95퍼센트 속도 겁나 느림

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        result = []
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        def dfs(x, y, val, cnt):
            for i in range(4):
                n_x, n_y = dx[i]+x, dy[i]+y
                if 0 <= n_x and n_x < len(matrix) and 0 <= n_y and n_y < len(matrix[0]):
                    n_val = matrix[n_x][n_y]
                    if val < n_val and dp[n_x][n_y] < cnt+1:
                        dp[n_x][n_y] = cnt + 1
                        dfs(n_x, n_y, n_val, cnt+1)
            
            result.append(cnt)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if dp[i][j] == 0:
                    dfs(i, j, matrix[i][j], 1)
        
        return max(result)

# 두 번째 풀이 dfs + dp
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix[0]), len(matrix)
        dp = [[0] * row for _ in range(col)]
        dc, dr = [1, -1, 0, 0], [0, 0, -1, 1]
        result = 0

        def dfs(c, r):
            if dp[c][r] != 0:
                return dp[c][r]
            
            temp = [0]
            for i in range(4):
                n_c, n_r = dc[i]+c, dr[i]+r
                if n_c >= 0 and n_r >= 0 and n_c < col and n_r < row and matrix[c][r] < matrix[n_c][n_r]:
                    temp.append(dfs(n_c, n_r))
            
            dp[c][r] = max(temp) + 1

            return dp[c][r]
        for c in range(col):
            for r in range(row):
                result = max(result, dfs(c, r))
        
        return result