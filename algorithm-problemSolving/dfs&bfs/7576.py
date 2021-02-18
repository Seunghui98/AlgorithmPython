#BOJ 7576 토마토.py
from collections import deque

m, n = map(int, input().split())
graph = []
queue = deque()

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):      
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny <m and graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y] + 1
          queue.append((nx, ny))

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
        queue.append((i, j))


bfs()

m = 1
what = True
for p in graph:
  for q in p:
    if q == 0:
      what = False
    m = max(m, q)

if what:
  print(m-1)
else:
  print(-1)
    
