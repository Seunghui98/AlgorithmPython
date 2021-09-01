# 카드2 - BOJ 2164
# 덱
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
stack = deque()
for i in range(n, 0, -1):
    stack.append(i)

while len(stack) > 1:
    stack.pop()
    first = stack.pop()
    stack.appendleft(first)

print(stack[0])


