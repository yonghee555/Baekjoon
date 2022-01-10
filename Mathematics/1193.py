# 분수찾기
# https://www.acmicpc.net/problem/1193

X = int(input())

i = 1
answer = 0
while X > answer:
    answer += i
    i += 1

if i % 2 == 0:
    print(answer - X + 1, end='')
    print('/', end='')
    print(i - answer + X - 1)
else:
    print(i - answer + X - 1, end='')
    print('/', end='')
    print(answer - X + 1)