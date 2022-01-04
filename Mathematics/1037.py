# 약수
# https://www.acmicpc.net/problem/1037

K = int(input())
divisor = list(map(int, input().split()))

divisor.sort()
print(divisor[0] * divisor[-1])