N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
	a, b = map(int, input().split())
	tree[a].append(b)
	tree[b].append(a)

node = [1]
ans = {}
check = [False for _ in range(N + 1)]

while len(node) > 0:
	parent = node.pop(0)
	for i in tree[parent]:
		if not check[i]:
			ans[i] = parent
			node.append(i)
			check[i] = True

for i in range(2, N + 1):
	print(ans[i])