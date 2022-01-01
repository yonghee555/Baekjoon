# 행렬 곱셈 순서
# https://www.acmicpc.net/problem/11049

import sys
input = sys.stdin.readline

N = int(input())
arrays = []
dp = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(N):
    r, c = map(int, input().split())
    arrays.append((r, c))

for i in range(2, N + 1):
    for j in range(1, N + 2 - i):
        dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] + arrays[j - 1][0] * arrays[j + k][0] * arrays[j + i - 2][1] for k in range(i - 1)])

print(dp[1][N])