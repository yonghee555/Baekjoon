# 정수 삼각형
# https://www.acmicpc.net/problem/1932

triangle = []
n = int(input())

for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    # j = 0
    triangle[i][0] += triangle[i - 1][0]
    # 0 < j < i
    for j in range(1, i):
        triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    # j = i
    triangle[i][i] += triangle[i - 1][i - 1]

print(max(triangle[n - 1]))