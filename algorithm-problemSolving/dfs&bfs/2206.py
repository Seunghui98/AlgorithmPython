#BOJ 벽 부수고 이동하기 2206번
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  queue = deque()
  queue.append((0, 0, 0))
  visited[0][0][0] = 1

  while queue:
    x, y, w = queue.popleft()
    if x == n-1 and y == m-1:
        return visited[x][y][w]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      
      if visited[nx][ny][w]:
        continue

      if graph[nx][ny] == 0:
        visited[nx][ny][w] = visited[x][y][w] + 1
        queue.append((nx, ny, w))
      if graph[nx][ny] == 1 and w == 0:
        visited[nx][ny][1] = visited[x][y][w] + 1
        queue.append((nx, ny, 1))
  return -1

print(bfs())
    



  
