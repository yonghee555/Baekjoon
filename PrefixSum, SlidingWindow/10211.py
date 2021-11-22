# Maximum Subarray
# https://www.acmicpc.net/problem/10211

T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    answer = -1000

    p_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        p_sum[i] = p_sum[i - 1] + data[i - 1]

    for i in range(1, N + 1):
        for j in range(0, i):
            subarray = p_sum[i] - p_sum[j]
            if answer < subarray:
                answer = subarray
    print(answer)