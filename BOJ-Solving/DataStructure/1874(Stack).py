# 스택 수열 - BOJ 1874
import sys

input = sys.stdin.readline

n = int(input())
number = []
answer = []
stack2 = []
stack = []
for _ in range(n):
    number.append(int(input()))

num = 0
what = False
for i in range(len(number)):
    if num < number[i]:
        for j in range(num+1, number[i]+1):
            stack2.append(j)
            answer.append('+')
        num = number[i]
        answer.append('-')
        stack.append(number[i])
        stack2.pop()
        continue
    else:
        top = stack2[-1]
        if top == number[i]:
            answer.append('-')
            stack.append(number[i])
            stack2.pop()
        elif top < number[i]:
            diff = top - number[i]
            for j in range(diff):
                stack2.pop()
                answer.append('-')
            stack.append(number[i])
        else:
            what = True
            break

if what:
    print('NO')
else:
    for i in answer:
        print(i)
