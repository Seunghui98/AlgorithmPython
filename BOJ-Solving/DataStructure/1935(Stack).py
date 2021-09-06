# 후위 표기식2 - BOJ 1935
# 스택 - 후위 표기식 - 
import sys

input = sys.stdin.readline

n = int(input())
cal = input().split()

data = []
for i in range(n):
    digit = int(input())
    data.append(digit)

stack = []

for c in cal[0]:
    if c.isalpha():
        stack.append(data[ord(c) - ord('A')])
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if c == "+":
            stack.append(n1+n2)
        elif c == '-':
            stack.append(n1-n2)
        elif c == '*':
            stack.append(n1*n2)
        elif c == '/':
            stack.append(n1/n2)

print(format(stack[0], ".2f"))
