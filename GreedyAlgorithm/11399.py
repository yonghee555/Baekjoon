# ATM
# https://www.acmicpc.net/problem/11399

n = int(input())
p = list(map(int, input().split()))

p.sort()
answer = 0
for i in range(1, n + 1):
    answer += sum(p[:i])

print(answer)