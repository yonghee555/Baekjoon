# 상근이의 여행
# https://www.acmicpc.net/problem/9372

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

t = int(input())
for _ in range(t):
    count = 0
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            count += 1
    print(count)