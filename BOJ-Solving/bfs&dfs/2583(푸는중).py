# 2583 - BOJ 보물섬
from collections import deque

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    max_n = 0
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0 and graph[x][y] != "W":
                visit[x][y] = 1
                graph[x][y] = graph[a][b] + 1
                max_n = max(max_n, graph[x][y])
                q.append([x, y])
    return max_n


result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != "W":
            visit = [[0]*m for _ in range(n)]
            graph[i][j] = 0
            visit[i][j] = 1
            result = max(result, bfs(i, j))


print(result)
