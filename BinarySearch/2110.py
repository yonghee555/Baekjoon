# 공유기 설치
# https://www.acmicpc.net/problem/2110

import sys

house = []

N, C = map(int, input().split())
for _ in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()

start = 1
end = house[-1] - house[0]

result = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    old = house[0]
    for i in range(1, N):
        if house[i] >= old + mid:
            count += 1
            old = house[i]

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)