# 유기농 배추
# https://www.acmicpc.net/problem/1012

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)