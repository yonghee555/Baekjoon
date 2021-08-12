def solve(current, n):
	if current == M:
		for n in stack:
			print(n, end = ' ')
		print()
	else:
		for i in range(n, N + 1):
			stack.append(i)
			solve(current + 1, i)
			stack.pop()

N, M = map(int, input().split())
stack = []
solve(0, 1)