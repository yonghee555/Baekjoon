# 최소공배수
# https://www.acmicpc.net/problem/1934

def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A * B // gcd(A, B))