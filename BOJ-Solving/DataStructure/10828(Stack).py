# BOJ 스택 - 10828번
import sys

input = sys.stdin.readline

stack_list = []

n = int(input())

for _ in range(n):
    data = input()
    if "push" in data:
        stack_list.append(int(data[5:]))
    else:
        if "pop" in data:
            if len(stack_list) == 0:
                print(-1)
            else:
                print(stack_list.pop())
        elif "size" in data:
            print(len(stack_list))
        elif "empty" in data:
            if len(stack_list) == 0:
                print(1)
            else:
                print(0)
        elif "top" in data:
            if len(stack_list) == 0:
                print(-1)
            else:
                print(stack_list[-1])
