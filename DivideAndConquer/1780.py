# 종이의 개수
# https://www.acmicpc.net/problem/1780

from collections import defaultdict

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != color:
                solution(x, y, N // 3)
                solution(x, y + N // 3, N // 3)
                solution(x, y + 2 * N // 3, N // 3)
                solution(x + N // 3, y, N // 3)
                solution(x + N // 3, y + N // 3, N // 3)
                solution(x + N // 3, y + 2 * N // 3, N // 3)
                solution(x + 2 * N // 3, y, N // 3)
                solution(x + 2 * N // 3, y + N // 3, N // 3)
                solution(x + 2 * N // 3, y + 2 * N // 3, N // 3)
                return
    answer[color] += 1

answer = defaultdict(int)
solution(0, 0, N)

print(answer[-1])
print(answer[0])
print(answer[1])