# 우주신과의 교감
# https://www.acmicpc.net/problem/1774

import sys
from math import sqrt, pow

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

n, m = map(int, input().split())
parent = [i for i in range(n)]
edges = []
vertices = []
answer = 0

for _ in range(n):
    x, y = map(int, input().split())
    vertices.append((x, y))

for i in range(n):
    for j in range(n):
        if i == j: continue
        distance = sqrt(pow(vertices[i][0] - vertices[j][0], 2) + pow(vertices[i][1] - vertices[j][1], 2))
        edges.append((i, j, distance))

edges.sort(key=lambda x : x[2])

for _ in range(m):
    x, y = map(int, input().split())
    union_parent(parent, x - 1, y - 1)

for edge in edges:
    a, b, distance = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += distance

print(format(answer, ".2f"))