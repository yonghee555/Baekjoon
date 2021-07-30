# 동전 0
# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())

result = 0
coins = []
for _ in range(n):
    coins.append(int(input()))

for coin in coins[::-1]:
    result += k // coin
    k %= coin

print(result)