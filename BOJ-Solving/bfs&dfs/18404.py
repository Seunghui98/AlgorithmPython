# 현명한 나이트 - BOJ 18404
# BFS
from collections import deque
n, m = map(int, input().split())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == -1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y]+1


x, y = map(int, input().split())
graph = [[-1]*n for _ in range(n)]
result = []

bfs(x-1, y-1)

for _ in range(m):
    a, b = map(int, input().split())
    result.append(graph[a-1][b-1])

for r in result:
    print(r, end=' ')
