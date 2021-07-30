# 주유소
# https://www.acmicpc.net/problem/13305

n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

cost = 0
i = 0

while i < n:
    price_now = prices[i]
    j = i + 1
    while j < n:
        if prices[j] < price_now:
            cost += price_now * sum(roads[i:j])
            i = j
            break
        j += 1
    if j == n:
        cost += price_now * sum(roads[i:])
        break

print(cost)
