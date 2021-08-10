# 2×n 타일링
# https://www.acmicpc.net/problem/11726

n = int(input())
d = [0] * (n + 1)

d[1] = 1
if n > 1:
    d[2] = 2
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 10007
print(d[n])