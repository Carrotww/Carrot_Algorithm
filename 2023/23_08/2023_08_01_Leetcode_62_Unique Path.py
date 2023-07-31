# https://leetcode.com/problems/unique-paths/

# dp 풀이

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        graph = [[0] * n for _ in range(m)]
        for i in range(n):
            graph[0][i] = 1

        for r in range(1, m):
            graph[r][0] = 1
            for c in range(1, n):
                graph[r][c] = graph[r][c-1] + graph[r-1][c]
        
        return graph[m-1][n-1]


# 메모리 효율 좋은 dp 풀이

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row_list = [1] * n

        for r in range(m-1):
            new_row_list = [0] * n
            new_row_list[0] = 1
            for c in range(1, n):
                new_row_list[c] = new_row_list[c-1] + row_list[c]
            row_list = new_row_list
        return row_list[-1]