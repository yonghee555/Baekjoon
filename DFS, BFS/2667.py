# 단지번호붙이기
# https://www.acmicpc.net/problem/2667

n = int(input())
graph = []
answer = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return 0
    if graph[x][y] == 1:
        graph[x][y] = 0
        return (1 + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x - 1, y) + dfs(x, y - 1))
    return 0

for i in range(n):
    for j in range(n):
        m = dfs(i, j)
        if m > 0:
            answer.append(m)
print(len(answer))
answer.sort()
for i in answer:
    print(i)