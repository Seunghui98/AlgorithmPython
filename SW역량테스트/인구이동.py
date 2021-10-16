# 인구이동 - BOJ 7285
# BFS + Queue
from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    connect = deque()
    connect_sum = 0
    connect_count = 0
    while q:
        x, y = q.popleft()
        connect.append((x, y))
        connect_sum += graph[x][y]
        connect_count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    diff = abs(graph[x][y]-graph[nx][ny])
                    if l <= diff <= r:
                        q.append((nx, ny))
                        visited[nx][ny] = True

    while connect:
        x, y = connect.popleft()
        graph[x][y] = (connect_sum // connect_count)
    if connect_count == 1:
        return 0
    else:
        return 1

answer = 0
while True:
    visited = [[False]* n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                count += bfs(i, j, visited)

    if count == 0:
        break
    else:
        answer += 1

print(answer)
