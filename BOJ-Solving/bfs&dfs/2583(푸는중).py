# 2583 - BOJ 보물섬
from collections import deque

n, m = map(int, input().split())
graph = [input() for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, visited, cnt):
    visited[x][y] = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                dfs(nx, ny, visited, cnt)

def bfs(x, y, visited, cnt):
    v = [[-1]*m for _ in range(n)]
    for i in range(n):
        print(v[i])
    v[x][y] = 0
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == cnt and v[nx][ny] == -1:
                    v[nx][ny] = v[x][y] + 1
                    q.append((nx, ny))
    mm = 0
    for i in range(n):
        mm = max(mm, max(v[i]))
        print(v[i])

    print(mm)
    print()
    return mm

answer = int(1e9)

visited = [[0] * m for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L' and visited[i][j] == 0:
            dfs(i, j, visited, cnt)
            answer = min(answer, bfs(i, j, visited, cnt))
            cnt += 1

print(answer)
