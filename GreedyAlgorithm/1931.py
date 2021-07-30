# 회의실 배정
# https://www.acmicpc.net/problem/1931

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x:(x[1], x[0]))

count = 1
end_time = meetings[0][1]
for i in range(1, n):
    if meetings[i][0] >= end_time:
        end_time = meetings[i][1]
        count += 1

print(count)