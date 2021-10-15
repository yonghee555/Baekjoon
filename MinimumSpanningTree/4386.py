# 별자리 만들기
# https://www.acmicpc.net/problem/4386

import sys, math
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

n = int(input())
vertices = []
parent = [i for i in range(n)]
edges = []
answer = 0

for _ in range(n):
    x, y = map(float, input().split())
    vertices.append((x, y))

for i in range(n):
    for j in range(n):
        if i == j: continue
        distance = math.sqrt(math.pow(vertices[i][0] - vertices[j][0], 2) + math.pow(vertices[i][1] - vertices[j][1], 2))
        edges.append((i, j, distance))

edges.sort(key=lambda x : x[2])
for edge in edges:
    a, b, cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print(format(answer, ".2f"))