# LCS 2
# https://www.acmicpc.net/problem/9252

s1 = input().rstrip()
s2 = input().rstrip()

d = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            d[i + 1][j + 1] = d[i][j] + 1
        else:
            d[i + 1][j + 1] = max(d[i][j + 1], d[i + 1][j])

print(max(sum(d, [])))

ans = ""
i, j = len(s1), len(s2)
now = d[i][j]
while now > 0:
    if d[i][j - 1] == d[i - 1][j] == now - 1:
        ans = s1[i - 1] + ans
        now -= 1
        i -= 1
        j -= 1
    elif d[i - 1][j] > d[i][j - 1]:
        i -= 1
    else:
        j -= 1
print(ans)
