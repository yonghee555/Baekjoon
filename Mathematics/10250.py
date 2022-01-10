# ACM 호텔
# https://www.acmicpc.net/problem/10250

from math import ceil

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if H == 1:
        print(1, end='')
        if N < 10:
            print(0, end='')
        print(N)
        continue
    floor = N % H
    if floor == 0:
        print(H, end='')
    else:
        print(floor, end='')
    room = ceil(N / H)
    if room < 10:
        print(0, end='')
    print(room)