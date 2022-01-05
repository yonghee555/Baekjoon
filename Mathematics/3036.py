# 링
# https://www.acmicpc.net/problem/3036

def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

N = int(input())
ring = list(map(int, input().split()))

for i in range(1, N):
    g = gcd(ring[0], ring[i])
    print('{0}/{1}'.format(ring[0]//g, ring[i]//g))