# 공주님을 구해라 ! - BOJ 17836
# BFS
from collections import deque

n, m, t = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
gonju = 10001

def bfs(a, b):
    global gonju
    q = deque()
    q.append((a, b, 0))
    visited[a][b] = 1

    while q:
        x, y, time = q.popleft()
        if x == n-1 and y == m-1:
            gonju = min(gonju, time)
            break
        if time+1 > t:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]==0:
                if graph[nx][ny] == 1:
                    continue
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, time+1))
                else:
                    visited[nx][ny] = 1
                    diff = time + 1 + abs(nx-(n-1)) + abs(ny-(m-1))
                    if diff <= t:
                        gonju = diff

bfs(0, 0)

if gonju > t:
    print('Fail')
else:
    print(gonju)
