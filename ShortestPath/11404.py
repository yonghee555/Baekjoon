# 플로이드
# https://www.acmicpc.net/problem/11404

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = float('inf')
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] != INF:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b or a == k or b == k:
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if graph[i][j] >= INF else graph[i][j], end=' ')
    print()