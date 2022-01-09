# 쿼드트리
# https://www.acmicpc.net/problem/1992

N = int(input())
video = [list(input()) for _ in range(N)]

def compress(x, y, N):
    global answer
    color = video[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if video[i][j] != color:
                answer += '('
                compress(x, y, N // 2)
                compress(x, y + N // 2, N // 2)
                compress(x + N // 2, y, N // 2)
                compress(x + N // 2, y + N // 2, N // 2)
                answer += ')'
                return
    if color == '0':
        answer += '0'
    else:
        answer += '1'

answer = ""
compress(0, 0, N)
print(answer)