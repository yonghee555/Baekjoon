# 감시 피하기
# https://www.acmicpc.net/problem/18428

graph = []
teachers = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
for _ in range(N):
    graph.append(list(map(str, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            teachers.append((i, j))

isTrue = False

def dfs(count):
    if count == 3:
        isSafe = True
        for x, y in teachers:
            for i in range(4):
                nx, ny = x, y
                while True:
                    nx, ny = nx + dx[i], ny + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        break
                    if graph[nx][ny] == 'O':
                        break
                    if graph[nx][ny] == 'S':
                        isSafe = False
                        break
                    continue
        if isSafe:
            global isTrue
            isTrue = True
        return

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                dfs(count)
                graph[i][j] = 'X'
                count -= 1

dfs(0)
if not isTrue:
    print('NO')
else:
    print('YES')