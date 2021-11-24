# 병사 배치하기
# https://www.acmicpc.net/problem/18353

N = int(input())
power = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if power[i] < power[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))