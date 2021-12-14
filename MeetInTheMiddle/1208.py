# 부분수열의 합 2
# https://www.acmicpc.net/problem/1208

from math import ceil
from itertools import combinations
from bisect import bisect_left, bisect_right

N, S = map(int, input().split())
array = list(map(int, input().split()))

array1 = array[:ceil(N / 2)]
array2 = array[ceil(N / 2):]

subset1 = []
subset2 = []

for i in range(1, len(array1) + 1):
    for c in combinations(array1, i):
        subset1.append(sum(c))

for i in range(1, len(array2) + 1):
    for c in combinations(array2, i):
        subset2.append(sum(c))

subset1.sort()
answer = 0

# 이진탐색 모듈을 이용해 S - i의 개수 찾아줌
for i in subset2:
    answer += bisect_right(subset1, S - i) - bisect_left(subset1, S - i) 

# subset1에서 0개, subset2에서 0개를 뽑는 경우 추가
answer += bisect_right(subset1, S) - bisect_left(subset1, S)
answer += subset2.count(S)
print(answer)