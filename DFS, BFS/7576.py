# 토마토
# https://www.acmicpc.net/problem/7576

from collections import deque

box = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

m, n = map(int, input().split())
for _ in range(n):
    box.append(list(map(int, input().split())))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))
bfs()
isTrue = False
result = -1
for row in box:
    for i in row:
        if i == 0:
            isTrue = True
        result = max(result, i)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
