# 합 구하기
# https://www.acmicpc.net/problem/11441

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
p_sum = [0] * (N + 1)

for i in range(1, N + 1):
    p_sum[i] = p_sum[i - 1] + numbers[i - 1]

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(p_sum[j] - p_sum[i - 1])