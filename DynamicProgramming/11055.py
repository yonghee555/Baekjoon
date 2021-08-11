# 가장 큰 증가하는 부분 수열
# https://www.acmicpc.net/problem/11055

from copy import deepcopy

n = int(input())
A = list(map(int, input().split()))

d = deepcopy(A)

for i in range(1, n):
    for j in range(0, i):
        if A[j] < A[i]:
            d[i] = max(d[i], d[j] + A[i])
print(max(d))