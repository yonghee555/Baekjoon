# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609

A, B = map(int, input().split())

def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

print(gcd(A, B))
print(A * B // gcd(A, B))