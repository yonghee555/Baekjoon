# 소수의 연속합
# https://www.acmicpc.net/problem/1644

from math import sqrt

N = int(input())

array = [True for _ in range(N + 1)]
prime = [] # N 이하의 소수를 담는 리스트

# 에라토스테네스의 체 이용하여 소수 판별
for i in range(2, int(sqrt(N)) + 1):
    if array[i]:
        j = 2
        while i * j <= N:
            array[i * j] = False
            j += 1

for i in range(2, N + 1):
    if array[i]:
        prime.append(i)

right = 0
tmp = 0
answer = 0

# 투 포인터
for left in range(len(prime)):
    while right < len(prime) and tmp < N:
        tmp += prime[right]
        right += 1
    if tmp == N:
        answer += 1
    tmp -= prime[left]

print(answer)