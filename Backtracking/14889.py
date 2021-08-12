# 스타트와 링크
# https://www.acmicpc.net/problem/14889

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

selected = [False for _ in range(N)]
answer = 2000

def dfs(i, cnt):
    if cnt == N // 2:
        global answer
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if selected[i] and selected[j]:
                    start += S[i][j]
                elif not selected[i] and not selected[j]:
                    link += S[i][j]
        answer = min(answer, abs(start - link))
        return

    for a in range(i, N):
        selected[a] = True
        dfs(a + 1, cnt + 1)
        selected[a] = False

dfs(0, 0)
print(answer)