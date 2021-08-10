# 피보나치 함수
# https://www.acmicpc.net/problem/1003

d_zero = [0] * 41
d_one = [0] * 41

d_zero[0] = 1
d_one[1] = 1

for i in range(2, 41):
    d_one[i] = d_one[i - 2] + d_one[i - 1]
    d_zero[i] = d_one[i - 1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(d_zero[N], d_one[N])