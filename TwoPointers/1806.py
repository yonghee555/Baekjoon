# 부분합
# https://www.acmicpc.net/problem/1806

N, S = map(int, input().split())
array = list(map(int, input().split()))
answer = N + 1

left = 0
right = 0
tmp = 0

for left in range(N):
    while right < N and tmp < S:
        tmp += array[right]
        right += 1
    if tmp >= S and answer > right - left:
        answer = right - left
    tmp -= array[left]

if answer == N + 1:
    print(0)
else:
    print(answer)