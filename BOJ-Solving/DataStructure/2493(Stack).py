# 2493 - BOJ 탑
# 스택, 구현
import sys

input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

stack = []
answer = [0] * n

for i in range(len(data)-1, -1, -1):
    if len(stack) == 0:
        stack.append([i, data[i]])
    else:
        while data[i] > stack[len(stack)-1][1]:
            top = stack.pop()
            answer[top[0]] = i+1
            if len(stack) == 0:
                break
        stack.append([i, data[i]])





for i in answer:
    print(i, end=' ')
