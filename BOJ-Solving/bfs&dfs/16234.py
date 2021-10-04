# 인구이동 - BOJ 16234
# BFS
import sys
from collections import deque

input = sys.stdin.readline
n, l, r = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

def bfs(a, b):
    connect = deque()
    q = deque()
    q.append((a, b))
    people, count = 0, 0
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        connect.append((x, y))
        count += 1
        people += graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    diff = abs(graph[x][y] - graph[nx][ny])
                    if l <= diff <= r:
                        visited[nx][ny] = count
                        q.append((nx, ny))
    while connect:
        x, y = connect.popleft()
        graph[x][y] = people // count
    if count == 1:
        return 0
    return 1


answer = 0

while True:
    q = deque()
    visited = [[0] * n for _ in range(n)]
    break_cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                break_cnt += bfs(i, j)
    if break_cnt == 0:
        break
    answer += 1

print(answer)
