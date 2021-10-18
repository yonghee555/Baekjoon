# N과 M (5)
# https://www.acmicpc.net/problem/15654

def dfs(current):
    if current == m:
        print(*stack)
    else:
        for i in range(n):
            if numbers[i] in stack:
                continue
            stack.append(numbers[i])
            dfs(current + 1)
            stack.pop()

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

stack = []
dfs(0)