# 절댓값 힙
# https://www.acmicpc.net/problem/11286

import heapq
import sys

input = sys.stdin.readline
q = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(q, (x, 1))
    elif x < 0:
        heapq.heappush(q, (-x, -1))
    elif q:
        x, op = heapq.heappop(q)
        print(x * op)
    else:
        print(0)