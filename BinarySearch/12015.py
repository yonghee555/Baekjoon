# 가장 긴 증가하는 부분 수열 2
# https://www.acmicpc.net/problem/12015

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [0]

for i in A:
    start = 1
    end = len(answer) - 1
    while start <= end:
        mid = (start + end) // 2
        if answer[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    if start >= len(answer):
        answer.append(i)
    else:
        answer[start] = i
print(len(answer) - 1)