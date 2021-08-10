# 파도반 수열
# https://www.acmicpc.net/problem/9461

d = [0] * 101

d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2

for i in range(6, 101):
    d[i] = d[i - 1] + d[i - 5]

T = int(input())
for _ in range(T):
    n = int(input())
    print(d[n])