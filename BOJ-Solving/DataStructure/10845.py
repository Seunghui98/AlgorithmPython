# 큐 -  BOJ 10845
#Queue
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    x = input().split()
    if len(x) == 2:
        q.append(int(x[1]))
    else:
        if "pop" in x[0]:
            if len(q) > 0:
                print(q.popleft())
            else:
                print(-1)
        elif "size" in x[0]:
            print(len(q))
        elif "empty" in x[0]:
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif "front" in x[0]:
            if len(q) > 0:
                print(q[0])
            else:
                print(-1)
        elif "back" in x[0]:
            if len(q) > 0:
                print(q[-1])
            else:
                print(-1)
