# 내리막 길
# https://www.acmicpc.net/problem/1520

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(i, j):
    if i == M - 1 and j == N - 1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 0
    for n in range(4):
        ni, nj = dir[n][0] + i, dir[n][1] + j
        if ni < 0 or ni >= M or nj < 0 or nj >= N:
            continue
        if graph[ni][nj] < graph[i][j]:
            dp[i][j] += dfs(ni, nj)
    return dp[i][j]

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
print(dfs(0, 0))