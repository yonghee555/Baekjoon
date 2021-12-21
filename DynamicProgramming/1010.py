# 다리 놓기
# https://www.acmicpc.net/problem/1010

def factorial(n):
    if n <= 1: 
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    if N == M:
        print(1)
        continue
    print(factorial(M) // (factorial(N) * factorial(M - N)))