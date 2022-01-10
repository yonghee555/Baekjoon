# 벌집
# https://www.acmicpc.net/problem/2292

N = int(input())

answer = 1
i = 1
while i < N:
    i += answer * 6
    answer += 1
print(answer)