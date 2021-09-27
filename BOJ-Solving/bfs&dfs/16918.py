# 봄버맨 - BOJ 16918
# 구현 + bfs
import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
r, c, n = map(int, input().split())
graph = [list(input()) for _ in range(r)]
# 1단계
n -= 1

def find():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                q.append((i, j))

def allBombSet():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 'O':
                graph[i][j] = 'O'

def bomb():
    while q:
        x, y = q.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == 'O':
                    graph[nx][ny] = '.'

while n:
    q = deque()
    # 2단계
    find()
    allBombSet()
    n -= 1
    if n == 0:
        break
    #3단계
    bomb()
    n -= 1

for i in range(r):
    for j in range(c):
        print(graph[i][j], end='')
    print()


