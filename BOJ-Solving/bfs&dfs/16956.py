# 늑대와 양 - BOJ 16956
# BFS 이동
import sys
from collections import deque

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a, b):
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <=nx<r and 0<=ny<c:
            if graph[nx][ny] == 'S':
                return False
            if graph[nx][ny] == '.':
                graph[nx][ny] = 'D'
    return True


what = False
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            if bfs(i, j):
                continue
            else:
                print(0)
                what = True
                break
    if what:
        break
if what:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            print(graph[i][j], end='')
        print()
