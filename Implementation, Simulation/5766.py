# 할아버지는 유명해!
# https://www.acmicpc.net/problem/5766

while True:
    players = [0] * 10001
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    for i in range(N):
        ranking = list(map(int, input().split()))
        for r in ranking:
            players[r] += 1
    second = sorted(players, reverse=True)[1]
    for i, p in enumerate(players):
        if p == second:
            print(i, end=' ')
    print()