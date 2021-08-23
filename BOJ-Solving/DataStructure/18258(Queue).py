# 큐2 - BOJ 18258
# 
import sys
from collections import deque

input = sys.stdin.readline

q = deque()
n = int(input())
for _ in range(n):
    x = input()
    if "push" in x:
        q.append(int(x[5:]))
    elif "pop" in x:
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif "size" in x:
        print(len(q))
    elif "empty" in x:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif "front" in x:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif "back" in x:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
