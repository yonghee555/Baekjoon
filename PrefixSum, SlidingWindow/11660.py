# 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = []
for _ in range(N):
    numbers.append(list(map(int, input().split())))

p_sum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        p_sum[i][j] = p_sum[i - 1][j] + numbers[i - 1][j - 1]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        p_sum[i][j] = p_sum[i][j - 1] + p_sum[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(p_sum[x2][y2] - p_sum[x2][y1 - 1] - p_sum[x1 - 1][y2] + p_sum[x1 - 1][y1 - 1])