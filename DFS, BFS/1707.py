# 이분 그래프
# https://www.acmicpc.net/problem/1707

import sys
sys.setrecursionlimit(10 ** 9)

def dfs(v, group):
    group = group % 2
    visited[v] = group
    for i in graph[v]:
        if visited[i] == -1:
            if not dfs(i, group + 1):
                return False
        elif visited[i] == visited[v]:
            return False
    return True
K = int(input())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    visited = [-1] * (V + 1)
    for _ in range(E):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    isTrue = True
    for i in range(1, V + 1):
        if visited[i] == -1:
            if not dfs(i, 0):
                isTrue = False
                break
    print('YES' if isTrue else 'NO')
