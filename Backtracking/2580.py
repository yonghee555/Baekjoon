# 스도쿠
# https://www.acmicpc.net/problem/2580

import sys

board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
n = len(zeros)

def check(num, i, j):
    for y in range(9):
        if y == j:
            continue
        if board[i][y] == num:
            return False
    for x in range(9):
        if x == i:
            continue
        if board[x][j] == num:
            return False
    for x in range(3):
        for y in range(3):
            nx, ny = i // 3 * 3 + x, j // 3 * 3 + y
            if (nx, ny) == (i, j):
                continue
            if num == board[nx][ny]:
                return False
    return True

def dfs(d):
    if d == n:
        for a in range(9):
            for b in range(9):
                print(board[a][b], end=' ')
            print()
        sys.exit(0)
    i, j = zeros[d]
    for a in range(1, 10):
        if check(a, i, j):
            board[i][j] = a
            dfs(d + 1)
            board[i][j] = 0
dfs(0)
