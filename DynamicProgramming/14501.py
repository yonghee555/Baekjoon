# 퇴사
# https://www.acmicpc.net/problem/14501

T = []
P = []

N = int(input())
dp = [0] * (N + 1)

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N - 1, -1, -1):
    if T[i] + i <= N:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]
print(dp[0])