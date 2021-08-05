# 나이트의 이동
# https://www.acmicpc.net/problem/7562

from collections import deque

dcol = [2, 1, -1, -2, -2, -1, 1, 2]
drow = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(col, row):
    queue = deque()
    queue.append((col, row))
    while queue:
        col, row = queue.popleft()
        if (col, row) == (target_col, target_row):
            return board[row][col] - 1
        for i in range(8):
            ncol, nrow = col + dcol[i], row + drow[i]
            if 0 <= ncol < l and  0 <= nrow < l and board[nrow][ncol] == 0:
                board[nrow][ncol] = board[row][col] + 1
                queue.append((ncol, nrow))
    print(board)

t = int(input())
for _ in range(t):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    col, row = map(int, input().split())
    target_col, target_row = map(int, input().split())
    if (col, row) == (target_col, target_row):
        print(0)
    else:  
        board[row][col] = 1
        print(bfs(col, row))