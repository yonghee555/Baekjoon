# ACM Craft
# https://www.acmicpc.net/problem/1005

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    answer = 0
    d = [0] + list(map(int, input().split()))
    dp = [i for i in d]
    q = deque()

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    w = int(input())

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        if now == w:
            break
        for i in graph[now]:
            dp[i] = max(dp[now] + d[i], dp[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    print(dp[w])