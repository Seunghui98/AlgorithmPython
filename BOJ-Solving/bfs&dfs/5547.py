# 일루미네이션 - BOJ 5547
# BFS

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
dx_odd = [-1, 1, 0, 0, -1, 1]
dy_odd = [0, 0, -1, 1, 1, 1]

dx_even = [-1, 1, 0, 0, -1, 1]
dy_even = [0, 0, 1, -1, -1, -1]

graph = [[0]*(m+2)]
isOut = [[0]*(m+2) for _ in range(n+2)]
for _ in range(n):
    data = [0]
    array = list(map(int, input().split()))
    for a in array:
        data.append(a)
    data.append(0)
    graph.append(data)

graph.append([0 for _ in range(m+2)])
def check_out(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        if x % 2 == 0:
            dx = dx_even
            dy = dy_even
        else:
            dx = dx_odd
            dy = dy_odd
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < (n+2) and 0 <= ny < (m+2):
                if (isOut[nx][ny] == 0):
                    if graph[nx][ny] == 0:
                        isOut[nx][ny] = 1
                        q.append((nx, ny))


check_out(0, 0)

count = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 0:
            continue
        if i % 2 ==0:
            dx = dx_even
            dy = dy_even
        else:
            dx = dx_odd
            dy = dy_odd
        for k in range(6):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n+2 and 0 <= ny <= m+2:
                if isOut[nx][ny] == 1:
                    count += 1

print(count)


