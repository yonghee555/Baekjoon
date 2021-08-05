# 벽 부수고 이동하기
# acmicpc.net/problem/2206

from collections import deque

graph = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input())))
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # visited[][][0]은 벽을 부수었을 때

def bfs():
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0][1] = 1
    while queue:
        x, y, w = queue.popleft()
        if (x, y) == (n - 1, m - 1):
            return visited[x][y][w]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append((nx, ny, 0))
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append((nx, ny, w))
    return -1
print(bfs())