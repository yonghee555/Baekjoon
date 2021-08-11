# 평범한 배낭
# https://www.acmicpc.net/problem/12865

w = [0] # 각 물건의 무게
v = [0] # 각 물건의 가치

N, K = map(int, input().split())

for _ in range(N):
    W, V = map(int, input().split())
    w.append(W)
    v.append(V)

# d[i][j] : i번째 물건까지로 j의 무게를 채운 가치핪의 최댓값
d = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if w[i] <= j:
            d[i][j] = max(d[i - 1][j], v[i] + d[i - 1][j - w[i]])
        else:
            d[i][j] = d[i - 1][j]
print(d[-1][-1])