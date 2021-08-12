def solve(current, result, add, sub, mul, div):
	global result_max
	global result_min
	if current == N - 1:
		result_max = max(result_max, result)
		result_min = min(result_min, result)
	else:
		current += 1
		if add > 0:
			solve(current, result + A[current], add - 1, sub, mul, div)
		if sub > 0:
			solve(current, result - A[current], add, sub - 1, mul, div)
		if mul > 0:
			solve(current, result * A[current], add, sub, mul - 1, div)
		if div > 0:
			solve(current, int(result / A[current]), add, sub, mul, div - 1)

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
result_max = -1000000000
result_min = 1000000000
solve(0, A[0], add, sub, mul, div)
print(result_max)
print(result_min)