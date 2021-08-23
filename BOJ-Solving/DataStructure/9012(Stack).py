# 괄호 - BOJ 9012
# 풀이법 - 스택
import sys

input = sys.stdin.readline


def Right(data):
    stack = []
    for i in data:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if len(stack) >= 1 and stack.pop() == "(":
                continue
            else:
                return False
    if len(stack) != 0:
        return False
    return True


n = int(input())

for _ in range(n):
    data = input()
    if Right(data):
        print("YES")
    else:
        print("NO")
