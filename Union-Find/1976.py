# 여행 가자
# https://www.acmicpc.net/problem/1976

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
m = int(input())

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i, j + 1)

plan = list(map(int, input().split()))
parent_first = find_parent(parent, plan[0])
for p in plan:
    if find_parent(parent, p) != parent_first:
        print('NO')
        break
else:
    print('YES')