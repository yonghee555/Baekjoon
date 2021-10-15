# 행성 터널
# https://www.acmicpc.net/problem/2887

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

vertices = []
edges = []
answer = 0

n = int(input())
parent = [i for i in range(n)]

for i in range(n):
    x, y, z = map(int, input().split())
    vertices.append((x, y, z, i))

for i in range(3):
    vertices.sort(key=lambda x: x[i])
    for j in range(n - 1):
        edges.append((vertices[j][3], vertices[j + 1][3], vertices[j + 1][i] - vertices[j][i]))

edges.sort(key=lambda x: x[2])
for edge in edges:
    a, b, cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print(answer)