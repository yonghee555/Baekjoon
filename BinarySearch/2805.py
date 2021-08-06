# 나무 자르기
# https://www.acmicpc.net/problem/2805

import sys

N, M = map(int, input().split())
trees = sorted(list(map(int, sys.stdin.readline().split())))

answer = 0
start = 0
end = max(trees)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            total += tree - mid
        if total >= M:
            answer = mid
            start = mid + 1
            break
    if total < M:
        end = mid - 1
print(answer)