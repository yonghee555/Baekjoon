# 랜선 자르기
# https://www.acmicpc.net/problem/1654

import sys

K, N = map(int, input().split())
cables = []
for _ in range(K):
    cables.append(int(sys.stdin.readline()))
cables.sort()
answer = 0

start = 0
end = max(cables)

while start <= end:
    mid = (start + end) // 2
    if mid == 0: # mid가 0인 경우 ZeroDivisionError 발생
        mid = 1
    total = 0
    for cable in cables:
        total += cable // mid
    if total < N:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)