# 마법사 상어와 파이어볼
# https://www.acmicpc.net/problem/20056

import sys
input = sys.stdin.readline

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    fireball = list(map(int, input().split()))
    board[fireball[0] - 1][fireball[1] - 1].append(fireball[2:])

for _ in range(k):
    new_board = [[[] for _ in range(n)] for _ in range(n)] # 이동한 후의 파이어볼들 위치 저장
    # 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for fireball in board[i][j]:
                    m, s, d = fireball
                    ni = (i + s * di[d]) % n
                    nj = (j + s * dj[d]) % n
                    new_board[ni][nj].append([m, s, d])

    # 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    for i in range(n):
        for j in range(n):
            if len(new_board[i][j]) > 1:
                nm, ns, nd = 0, 0, 0
                cnt = len(new_board[i][j])
                for fireball in new_board[i][j]:
                    nm += fireball[0]
                    ns += fireball[1]
                    nd += fireball[2] % 2
                nm = int(nm / 5) # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
                ns = int(ns / cnt) # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
                new_board[i][j] = []
                if nm == 0: # 질량이 0인 파이어볼은 소멸되어 없어진다.
                    continue
                # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
                if nd == 0 or nd == cnt:
                    for x in range(4):
                        new_board[i][j].append([nm, ns, x * 2])
                else:
                    for x in range(4):
                        new_board[i][j].append([nm, ns, x * 2 + 1])
    board = new_board

answer = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            for fireball in board[i][j]:
                answer += fireball[0]
print(answer)