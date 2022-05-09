# BOJ - 쉬운 최단 거리(14940번)
# BFS
import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
s_x = -1
s_y = -1
graph = []
board = [[0] * m for _ in range(n)]
def bfs(s_x, s_y):
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((s_x, s_y, 0))
    board[s_x][s_y] = 0
    visited[s_x][s_y] = True
    while q:
        x, y, dis = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    board[nx][ny] = dis+1
                    q.append((nx, ny, dis+1))



for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] == 2:
            s_x, s_y = i, j


bfs(s_x, s_y)

for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1 and board[i][j] == 0):
            print(-1, end=' ')
        else:
            print(board[i][j], end=' ')
    print()





