import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False:
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        visited[nx][ny] = True
                        continue
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))

def check():
    one_count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                one_count += 1
    return one_count


time = 0
last_cheese = 0

while True:
    cheese = check()
    if cheese > 0:
        bfs(0, 0)
        time += 1
        last_cheese = cheese
    elif cheese == 0:
        break

print(time)
print(last_cheese)
