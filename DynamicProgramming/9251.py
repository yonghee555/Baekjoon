# LCS
# https://www.acmicpc.net/problem/9251

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