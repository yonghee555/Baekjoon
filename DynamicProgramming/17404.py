# RGB거리 2
# https://www.acmicpc.net/problem/17404

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')

for c1 in range(3): # 1번 집의 색이 빨강, 초록, 파랑일 경우
    dp = [[0] * 3 for _ in range(N)] # 리스트 초기화

    for i in range(3): # dp[0] 초기화, 시작 색상인 경우만 cost[0][i]의 값으로 초기화
        if i == c1:
            dp[0][i] = cost[0][i]
        else:
            dp[0][i] = float('inf')

    for i in range(1, N):
        dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    for i in range(3):
        if i == c1: # N번 집의 색과 1번 집이 같은 경우는 고려하지 않음
            continue
        answer = min(answer, dp[N - 1][i])

print(answer)