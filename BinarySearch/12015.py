# 가장 긴 증가하는 부분 수열 2
# https://www.acmicpc.net/problem/12015

import sys
from bisect import bisect_left

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
dp = []

for i in A:
    k = bisect_left(dp, i)
    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i
print(len(dp))