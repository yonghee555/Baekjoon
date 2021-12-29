# 1로 만들기 2
# https://www.acmicpc.net/problem/12852

dp = [0] * 1000001
x = [0] * 1000001

N = int(input())

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    x[i] = i - 1
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        x[i] = i // 3
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        x[i] = i // 2

print(dp[N])
while N:
    print(N, end=" ")
    N = x[N]