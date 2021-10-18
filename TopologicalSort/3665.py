# 최종 순위
# https://www.acmicpc.net/problem/3665

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    indegree = [0] * (n + 1)
    result = []
    graph = [[] for _ in range(n + 1)]
    q = deque()
    impossible = True

    last_year = list(map(int, input().split()))
    for i in range(n):
        graph[last_year[i]] = last_year[i + 1:]
        indegree[last_year[i]] += i

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())

        if b in graph[a]:
            graph[b].append(a)
            graph[a].remove(b)
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a].append(b)
            graph[b].remove(a)
            indegree[a] -= 1
            indegree[b] += 1

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) < n:
        print('IMPOSSIBLE')
    else:
        print(*result)