# 집합
# https://www.acmicpc.net/problem/11723

import sys
input = sys.stdin.readline

def add(S, x):
    return S | (1 << x)

def remove(S, x):
    return S & ~(1 << x)

def check(S, x):
    if S & (1 << x):
        return 1
    else:
        return 0

def toggle(S, x):
    return S ^ (1 << x)

def all():
    return int(0b11111111111111111111)

def empty():
    return 0

S = 0

M = int(input())
for _ in range(M):
    line = input().rstrip()
    if line == 'all':
        S = all()
    elif line == 'empty':
        S = empty()
    else:
        operation, x = line.split()
        if operation == 'add':
            S = add(S, int(x) - 1)
        if operation == 'remove':
            S = remove(S, int(x) - 1)
        if operation == 'check':
            print(check(S, int(x) - 1))
        if operation == 'toggle':
            S = toggle(S, int(x) - 1)