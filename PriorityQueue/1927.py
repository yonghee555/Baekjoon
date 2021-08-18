# 최소 힙
# https://www.acmicpc.net/problem/1927

import heapq
import sys

input = sys.stdin.readline
q = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(q, x)
    elif q:
        print(heapq.heappop(q))
    else:
        print(0)