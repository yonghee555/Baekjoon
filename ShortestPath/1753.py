# 최단경로
# https://www.acmicpc.net/problem/1753

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

distances = [float('inf')] * (V + 1)
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

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

dijkstra(K)
for i in range(1, V + 1):
    print("INF" if distances[i] == float('inf') else distances[i])