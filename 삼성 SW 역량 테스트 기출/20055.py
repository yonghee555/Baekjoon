# 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
durablity = list(map(int, input().split()))

robot = [False] * 2 * n # i번째 칸에 로봇이 올려져 있는지 여부
start = 0 # 올리는 위치
end = n - 1 # 내리는 위치

answer = 0 # 단계
while True:
    answer += 1
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    start = (start - 1) % (2 * n)
    end = (end - 1) % (2 * n)
    robot[end] = False

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    if True in robot:
        for i in range(n):
            current = (end - i) % (2 * n)
            next = (current + 1) % (2 * n)
            if robot[current] and not robot[next] and durablity[next] > 0:
                robot[current], robot[next] = False, True
                durablity[next] -= 1
        robot[end] = False

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if durablity[start] > 0:
        robot[start] = True
        durablity[start] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if durablity.count(0) >= k:
        break

print(answer)