# 할 일 정하기 1
# https://www.acmicpc.net/problem/1311

INF = float('inf')
N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
# dp[x][visited] : 그 전까지 방문한 조합이 visited이고, x번째 사람일 때의 최소값
dp = [[-1] * (1 << N) for _ in range(20)]


def dfs(x, visited):
    if visited == (1 << N) - 1: # 모든 사람을 탐색한 경우
        return 0
    if dp[x][visited] != -1: # 이미 탐색한 경우
        return dp[x][visited]

    dp[x][visited] = INF
    for i in range(N):
        if visited & (1 << i): # i를 이미 선택한 경우 넘어감
            continue
        dp[x][visited] = min(dp[x][visited], dfs(x + 1, visited | (1 << i)) + D[x][i])
    return dp[x][visited]

print(dfs(0, 0))