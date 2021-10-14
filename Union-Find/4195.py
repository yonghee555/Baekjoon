# 친구 네트워크
# https://www.acmicpc.net/problem/4195

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[b] = a
        cnt[a] += cnt[b]

t = int(input())
for _ in range(t):
    parent = {}
    cnt = {}
    f = int(input())
    for _ in range(f):
        p1, p2 = input().split()
        if p1 not in parent:
            parent[p1] = p1
            cnt[p1] = 1
        if p2 not in parent:
            parent[p2] = p2
            cnt[p2] = 1
        union_parent(parent, p1, p2)
        print(cnt[find_parent(parent, p1)])