# 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
p_sum = [0] * (N + 1)

for i in range(1, N + 1):
    p_sum[i] = p_sum[i - 1] + numbers[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(p_sum[j] - p_sum[i - 1])