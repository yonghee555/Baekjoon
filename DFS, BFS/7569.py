# 토마토
# https://www.acmicpc.net/problem/7569

from collections import deque

box = []
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
queue = deque()

m, n, h = map(int, input().split())
for i in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, input().split())))
    box.append(tmp)

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if nx >= 0 and ny >= 0 and nz >= 0 and nx < h and ny < n and nz < m and box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1
                queue.append((nx, ny, nz))
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k))
bfs()
isTrue = False
result = -1
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                isTrue = True
            result = max(result, k)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
