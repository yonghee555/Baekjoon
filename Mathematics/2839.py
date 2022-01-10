# 설탕 배달
# https://www.acmicpc.net/problem/2839

N = int(input())

if N % 5 == 0:
    print(N // 5)
else:
    n3 = 1
    n5 = 0
    for i in range(N // 5 + 1):
        if (N - i * 5) % 3 == 0:
            n3 = (N - i * 5) // 3
            n5 = i
    if n3 * 3 + n5 * 5 == N:
        print(n3 + n5)
    else:
        print(-1)