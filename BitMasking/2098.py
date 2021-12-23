# 외판원 순회
# https://www.acmicpc.net/problem/2098

INF = int(1e9)
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(x, visited):
    if visited == (1 << N) - 1:
        if W[x][0]:
            return W[x][0]
        else: # 경로가 없을 때
            return INF
    if dp[x][visited] != -1:
        return dp[x][visited]

    dp[x][visited] = INF
    for i in range(1, N):
        if not W[x][i]: # 경로가 없으면 continue
            continue
        if visited & (1 << i): # 이미 방문했으면 continue
            continue
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + W[x][i])
    return dp[x][visited]

# 0번째에서 시작하여 0번째로 돌아오는 경로 탐색, Cycle이므로 어디에서 시작해도 동일
print(dfs(0, 1))