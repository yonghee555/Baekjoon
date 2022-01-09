# 곱셈
# https://www.acmicpc.net/problem/1629

A, B, C = map(int, input().split())

def multiply(A, B, C):
    if B == 1:
        return A % C
    half = multiply(A, B // 2, C)
    if B % 2 == 0:
        return half * half % C
    return half * half * A % C

print(multiply(A, B, C))