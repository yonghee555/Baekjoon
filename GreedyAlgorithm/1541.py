# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

numbers = list(map(str, input().split('-')))

first = sum(map(int, numbers[0].split('+')))

for n in numbers[1:]:
    if '+' in n:
        first -= sum(map(int, n.split('+')))
    else:
        first -= int(n)
print(first)