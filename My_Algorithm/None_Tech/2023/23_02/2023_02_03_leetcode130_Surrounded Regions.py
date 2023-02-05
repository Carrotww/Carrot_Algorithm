# https://leetcode.com/problems/surrounded-regions/

from typing import List

# 첫 번째 풀이, 속도 느림 다른 풀이로 다시 풀어보기
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        stack = []
        dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and visited[i][j] == 0:
                    temp = []
                    stack.append((i, j))
                    temp.append((i, j))
                    change = 1
                    while stack:
                        x, y = stack.pop()
                        visited[x][y] = 1
                        for di in range(4):
                            n_x, n_y = x+dx[di], y+dy[di]
                            if (n_x < 0 or n_x >= len(board)) or (n_y < 0 or n_y >= len(board[0])):
                                change = 0
                                continue
                            if visited[n_x][n_y] == 0 and board[n_x][n_y] == "O":
                                stack.append((n_x, n_y))
                                temp.append((n_x, n_y))
                    if change == 1:
                        for te in temp:
                            board[te[0]][te[1]] = "X"

        return board