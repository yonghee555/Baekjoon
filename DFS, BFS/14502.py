# 연구소
# https://www.acmicpc.net/problem/14502

from collections import deque
from itertools import combinations
from copy import deepcopy

viruses = deque() # 바이러스 위치 저장
answer = 0

def bfs(graph):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deepcopy(viruses)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))
    global answer
    result = sum(graph, [])
    answer = max(answer, result.count(0))

N, M = map(int, input().split())
graph = []
zeros = [] # 0의 위치
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zeros.append((i, j))
        elif graph[i][j] == 2:
            viruses.append((i, j))

for c in combinations(zeros, 3): # 벽을 놓을 위치 3개 선택
    new_graph = deepcopy(graph)
    for i, j in c:
        new_graph[i][j] = 1
    bfs(new_graph) # 벽 3개를 놓은 후의 그래프로 BFS 실행

print(answer)