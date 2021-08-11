# 포도주 시식
# https://www.acmicpc.net/problem/2156

wine = [0]
d = [0] * 10001

n = int(input())
for _ in range(n):
    wine.append(int(input()))

d[1] = wine[1]
if n > 1:
    d[2] = wine[1] + wine[2]

for i in range(3, n + 1):
    d[i] = wine[i] + max(max(d[:i - 2]) + wine[i - 1], max(d[:i - 1]))

print(max(d))