# 2×n 타일링 2
# https://www.acmicpc.net/problem/11727

n = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = d[i - 1] + 2 * d[i - 2] % 10007
print(d[n] % 10007)