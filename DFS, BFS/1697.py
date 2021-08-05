# 숨바꼭질
# https://www.acmicpc.net/problem/1697

from collections import deque

graph = [0] * 1000001
n, k = map(int, input().split())

def bfs():
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            print(graph[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000 and graph[nx] == 0:
                graph[nx] = graph[x] + 1
                queue.append(nx)

bfs()