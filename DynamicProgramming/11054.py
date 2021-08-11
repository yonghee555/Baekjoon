# 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054

n = int(input())
A = list(map(int, input().split()))

d = [[1, 1] for _ in range(n)] # 계속 증가 / 증가하다가 감소

for i in range(1, n):
    for j in range(0, i):
        if A[j] < A[i]:
            d[i][0] = max(d[i][0], d[j][0] + 1)
            # 계속 증가하는 경우가 더 클 경우에만 바꿔줌
            d[i][1] = max(d[i][0], d[i][1])
        elif A[j] > A[i]:
            d[i][1] = max(d[i][1], d[j][1] + 1)
# 이차원 리스트를 일차원 리스트로 합쳐준 후 최댓값 출력
print(max(sum(d, [])))