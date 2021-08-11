# 연속합
# https://www.acmicpc.net/problem/1912

n = int(input())
numbers = list(map(int, input().split()))

d = [0] * n
d[0] = numbers[0]

for i in range(1, n):
    d[i] = max(numbers[i] + d[i - 1], numbers[i])
print(max(d))