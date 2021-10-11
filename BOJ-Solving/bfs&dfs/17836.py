import sys
from collections import deque

input = sys.stdin.readline


n, m, t = map(int, input().split())
visited = [[10001] * m for _ in range(n)]

graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a, b):
    q = deque()
    q.append((a, b, 0))
    visited[a][b] = 0

    while q:
        x, y, w = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if w == 1:
                    if visited[nx][ny] >  visited[x][y] + 1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny, w))
                else:
                    if graph[nx][ny] == 1:
                        continue
                    elif graph[nx][ny] == 2:
                        if visited[nx][ny] > visited[x][y] + 1:
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx, ny, 1))
                    else:
                        if visited[nx][ny] > visited[x][y] + 1:
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx, ny, w))


bfs(0, 0)

if visited[n-1][m-1] > t:
    print('Fail')
else:
    print(visited[n-1][m-1])
