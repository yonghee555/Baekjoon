# 냅색문제
# https://www.acmicpc.net/problem/1450

from math import ceil
from itertools import combinations

N, C = map(int, input().split())
array = list(map(int, input().split()))

A1 = array[:ceil(N / 2)]
A2 = array[ceil(N / 2):]

subset1 = []
subset2 = []

for n in range(len(A1) + 1):
    for c in combinations(A1, n):
        subset1.append(sum(c))

for n in range(len(A2) + 1):
    for c in combinations(A2, n):
        subset2.append(sum(c))

subset1.sort() # 이진탐색을 하기 위하여 정렬
answer = 0

for i in subset2:
    if i > C:
        continue

    start = 0
    end = len(subset1)

    # 이진탐색 이용, lower bound
    while start < end:
        mid = (start + end) // 2
        if i + subset1[mid] > C:
            end = mid
        else:
            start = mid + 1
    answer += end

print(answer)