# 전깃줄
# https://www.acmicpc.net/problem/2565

wires = []
n = int(input())
for _ in range(n):
    wires.append(list(map(int, input().split())))
wires.sort()

d = [1] * n

for i in range(n):
    for j in range(i):
        if wires[i][1] > wires[j][1]:
            d[i] = max(d[i], d[j] + 1)
print(n - max(d))