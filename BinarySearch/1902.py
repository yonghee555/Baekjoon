# 수 찾기
# https://www.acmicpc.net/problem/1920

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
X = list(map(int, input().split()))

for i in X:
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == i:
            print(1)
            break
        elif A[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    else:
        print(0)