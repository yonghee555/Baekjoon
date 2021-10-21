# 청소년 상어
# https://www.acmicpc.net/problem/19236

from copy import deepcopy

graph = [[] for _ in range(4)]
fish = [[] for _ in range(16)]
answer = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(x, y, d, cnt):
    global graph, fish, answer
    move_fish(x, y)
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            answer = max(answer, cnt)
            return
        if not graph[nx][ny]:
            x, y = nx, ny
            continue

        temp_graph = deepcopy(graph)
        temp_fish = deepcopy(fish)
        fish_eat = graph[nx][ny]
        fish[graph[nx][ny][0]] = []
        graph[nx][ny] = []
        dfs(nx, ny, fish_eat[1], cnt + fish_eat[0] + 1)
        graph = temp_graph
        fish = temp_fish
        x, y = nx, ny

def move_fish(shark_x, shark_y):
    for i in range(16):
        if fish[i]:
            x, y = fish[i][0], fish[i][1]
            for _ in range(9):
                nx, ny = x + dx[graph[x][y][1]], y + dy[graph[x][y][1]]
                if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx, ny) == (shark_x, shark_y):
                    graph[x][y][1] = (graph[x][y][1] + 1) % 8
                    continue
                if graph[nx][ny]:
                    fish[graph[nx][ny][0]] = [x, y]
                graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
                fish[i] = [nx, ny]
                break

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        graph[i].append([data[2 * j] - 1, data[2 * j + 1] - 1])
        fish[data[2 * j] - 1] = [i, j]

shark_d = graph[0][0][1]
answer += graph[0][0][0] + 1
fish[graph[0][0][0]] = []
graph[0][0] = []
dfs(0, 0, shark_d, answer)
print(answer)