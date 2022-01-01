# 파일 합치기
# https://www.acmicpc.net/problem/11066

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    dp = [[0] * (K + 1) for _ in range(K + 1)]
    psum = [0] * (K + 1)

    # 누적합 계산
    for i in range(K):
        psum[i + 1] = psum[i] + files[i]

    for i in range(2, K + 1): # 합칠 파일의 수
        for j in range(1, K + 2 - i): # 시작 파일
            dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1)]) + psum[j + i - 1] - psum[j - 1]

    print(dp[1][K]) # 1부터 K까지 파일의 합 최소비용 출력