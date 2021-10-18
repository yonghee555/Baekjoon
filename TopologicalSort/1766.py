# 문제집
# https://www.acmicpc.net/problem/1766

import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

q = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)

print(*result)