# 두 수의 합
# https://www.acmicpc.net/problem/3273

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
x = int(input())

array.sort()
i, j = 0, n - 1
answer = 0
while i < j:
    s = array[i] + array[j]
    if s == x:
        answer += 1
        i += 1
    elif s > x:
        j -= 1
    else:
        i += 1
print(answer)