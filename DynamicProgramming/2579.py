# 계단 오르기
# https://www.acmicpc.net/problem/2579

score = [0] * 301
stair = [0]
n = int(input())

for _ in range(n):
    stair.append(int(input()))
score[1] = stair[1]
if n > 1:
    score[2] = stair[1] + stair[2]
for i in range(3, n + 1):
    score[i] = stair[i] + max(stair[i - 1] + score[i - 3], score[i - 2])
print(score[n])