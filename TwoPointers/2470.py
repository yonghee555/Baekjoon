# 두 용액
# https://www.acmicpc.net/problem/2470

N = int(input())
array = sorted(list(map(int, input().split())))

left = 0
right = N - 1

answer = [0, 0]
max_sum = 2000000001

if array[0] > 0: # 전부 산성 용액인 경우
    print(array[0], array[1])
elif array[N - 1] < 0: # 전부 알칼리성 용액인 경우
    print(array[N - 2], array[N - 1])
else:
    while left < right:
        tmp = array[left] + array[right]
        if tmp == 0:
            print(array[left], array[right])
            break
        if abs(tmp) < max_sum:
            answer = array[left], array[right]
            max_sum = abs(tmp)
        if tmp > 0:
            right -= 1
        else:
            left += 1
    else:
        print(*answer)