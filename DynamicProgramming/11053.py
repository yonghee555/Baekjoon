# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

n = int(input())
A = list(map(int, input().split()))

d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if A[j] < A[i]:
            d[i] = max(d[i], d[j] + 1)
print(max(d))