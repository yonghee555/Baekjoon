# 미확인 도착지
# https://www.acmicpc.net/problem/9370

import sys, heapq
input = sys.stdin.readline
INF = int(1e9) # float('inf')를 사용하였을 때 오답이 나왔다.

def dijkstra(start):
    q = []
    distances = [INF] * (n + 1)
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
    return distances

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    candidates = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    for _ in range(t):
        x = int(input())
        candidates.append(x)
    answer = []

    from_s = dijkstra(s)
    from_g = dijkstra(g)
    from_h = dijkstra(h)

    for x in candidates:
        if from_s[g] + from_g[h] + from_h[x] == from_s[x]: # s -> g -> h -> x가 s -> x 최단 거리와 같을 때
            answer.append(x)
        elif from_s[h] + from_h[g] + from_g[x] == from_s[x]: # s -> h -> g -> x가 s -> x 최단 거리와 같을 때
            answer.append(x)

    print(*sorted(answer))