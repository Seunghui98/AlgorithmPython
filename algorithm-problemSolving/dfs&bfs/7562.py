#BOJ 나이트의 이동 7562번
from collections import deque

t = int(input())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]
result = []
def bfs(x1, y1, x2, y2):
  queue = deque()
  queue.append([x1, y1])
  graph[x1][y1] = 1
  while queue:
      x, y = queue.popleft()
      if x == x2 and y == y2:
        result.append(graph[x][y]-1)
        return

      for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < l and 0 <= ny < l and not graph[nx][ny]:
          graph[nx][ny] = graph[x][y] + 1
          queue.append([nx, ny])


for _ in range(t):
  l = int(input())
  graph = [[0] * l for _ in range(l)]
  queue = deque()
  x1, y1 = map(int, input().split())
  x2, y2 = map(int, input().split())
  bfs(x1, y1, x2, y2)


for p in result:
  print(p)
