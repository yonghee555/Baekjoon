# 바이러스
# https://www.acmicpc.net/problem/2606

from collections import deque

n = int(input())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(graph, v, visited):
    visited[v] = True
    for i in range(1, n + 1):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in range(1, n + 1):
            if graph[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)
answer = visited.count(True)
print(answer - 1 if answer >= 1 else answer)
