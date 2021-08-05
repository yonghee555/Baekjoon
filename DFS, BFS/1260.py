# DFS와 BFS
# https://www.acmicpc.net/problem/1260

from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)
