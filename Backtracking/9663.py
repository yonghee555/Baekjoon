# N-Queen
# https://www.acmicpc.net/problem/9663

N = int(input())

def check(i):
    j = 0
    while i > j:
        if board[i] == board[j] or (abs(board[i] - board[j]) == i - j): return False
        j += 1
    return True

def dfs(i):
    if i == N:
        if check(i - 1): 
            global count
            count += 1
        return
    for x in range(N):
        board[i] = x
        if check(i):
            dfs(i + 1)

board = [0] * N
count = 0

dfs(0)
print(count)