from sys import stdin
from collections import deque

V = int(input())
graph = [[] for _ in range(V + 1)]

for i in range(V):
	line = list(map(int, stdin.readline().split()))
	for a in range(1, len(line) - 2, 2):
		graph[line[0]].append((line[a], line[a + 1]))

def bfs(start):
	q = deque()
	q.append(start)
	visit = [-1] * (V + 1)
	visit[start] = 0
	result = [0, 0]

	while q:
		t = q.popleft()
		for e, w in graph[t]:
			if visit[e] == -1:
				visit[e] = visit[t] + w
				q.append(e)
				if result[0] < visit[e]:
					result = visit[e], e

	return result

distance, node = bfs(1)
distance, node = bfs(node)
print(distance)
