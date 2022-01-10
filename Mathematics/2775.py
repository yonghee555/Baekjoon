# 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775

def people(k, n):
    if k == 0:
        return n
    if n == 1:
        return 1
    return people(k, n - 1) + people(k - 1, n)

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(people(k, n))