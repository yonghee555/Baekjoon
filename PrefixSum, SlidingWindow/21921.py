# 블로그
# https://www.acmicpc.net/problem/21921

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

answer = 0
count = 1
start = 0
end = X
sum_visitors = sum(visitors[start:end])
answer = sum_visitors

for i in range(1, N - X + 1):
    sum_visitors += visitors[end]
    sum_visitors -= visitors[start]
    start += 1
    end += 1
    if sum_visitors == answer:
        count += 1
    elif sum_visitors > answer:
        answer = sum_visitors
        count = 1

if answer == 0:
    print('SAD')
else:
    print(answer)
    print(count)