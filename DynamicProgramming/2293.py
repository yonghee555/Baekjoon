# 동전 1
# https://www.acmicpc.net/problem/2293

n, k = map(int, input().split())

d = [0] * (k + 1)
for _ in range(n):
    c = int(input())
    if c <= k:
        d[c] += 1
        for i in range(c, k + 1):
            d[i] += d[i - c]

print(d[k])