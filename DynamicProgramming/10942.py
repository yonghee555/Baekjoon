# 팰린드롬?
# https://www.acmicpc.net/problem/10942

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]

for i in range(N): # 수열의 길이
    for start in range(N - i):
        end = start + i

        if i == 0: # 수 1개
            dp[start][end] = 1
            continue
        if numbers[start] == numbers[end]:
            if i == 1: # 수 2개
                dp[start][end] = 1
            elif dp[start + 1][end - 1]:
                dp[start][end] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])