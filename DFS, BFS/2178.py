# 미로 탐색
# https://www.acmicpc.net/problem/2178

from collections import deque

n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    print(graph[n - 1][m - 1])

bfs(0, 0)