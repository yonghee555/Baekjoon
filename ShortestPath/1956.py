# 운동
# https://www.acmicpc.net/problem/1956

import sys

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
graph = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(V + 1):
    for a in range(V + 1):
        for b in range(V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = INF
for i in range(1, V + 1):
    answer = min(answer, graph[i][i])
print(-1 if answer >= INF else answer)