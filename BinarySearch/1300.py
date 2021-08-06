# K번째 수
# https://www.acmicpc.net/problem/1300

N = int(input())
k = int(input())

start = 1
end = N * N

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(1, N + 1):
        total += min(N, mid // i)
    if total >= k:
        end = mid - 1
        result = mid
    else:
        start = mid + 1
print(result)