# 숫자 카드 2
# https://www.acmicpc.net/problem/10816

import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

def binary_search(array:list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return array[start:end + 1].count(target)
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

answers = {}
for i in numbers:
    if i not in answers:
        answers[i] = binary_search(cards, i, 0, N - 1)
        
print(' '.join(str(answers[c]) if c in answers else '0' for c in numbers))