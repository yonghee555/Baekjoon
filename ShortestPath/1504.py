# 특정한 최단 경로
# https://www.acmicpc.net/problem/1504

import sys
import heapq

input = sys.stdin.readline
INF = float('inf')
N, E = map(int, input().split())

distances = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    distances[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
p1 = distances[v1]
p2 = distances[v2]

distances = [INF] * (N + 1)
dijkstra(v1)
p1 += distances[v2]
p2 += distances[N]

distances = [INF] * (N + 1)
dijkstra(v2)
p1 += distances[N]
p2 += distances[v1]

answer = min(p1, p2)
print(-1 if answer >= INF else answer)