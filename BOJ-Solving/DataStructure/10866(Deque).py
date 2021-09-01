# 덱 - BOJ 10866
# 덱 사용
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
d = deque()

for _ in range(n):
    x = input()
    if "push_front" in x:
        x_l = x.split()
        d.appendleft(int(x_l[1]))
    elif "push_back" in x:
        x_l = x.split()
        d.append(int(x_l[1]))
    elif "pop_front" in x:
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif "pop_back" in x:
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif "size" in x:
        print(len(d))
    elif "empty" in x:
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif "front" in x:
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif "back" in x:
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
