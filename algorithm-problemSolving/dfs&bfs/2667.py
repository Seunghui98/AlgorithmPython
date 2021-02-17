# BOJ 단지번호 붙이기 2667
from collections import deque
n = int(input())

graph = []
result = []

for _ in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  cnt = 1
  
  queue = deque()
  queue.append((x,y))
  graph[x][y] = 0
  # 주어진 범위 벗어나면 즉시 종료

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx <= -1 or ny <= -1 or nx >= n or ny >= n:
        continue
      if graph[nx][ny] == 0:
        continue

      # 현재 노드를 아직 방문하지 않았다면 방문 처리
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        cnt += 1
        queue.append((nx, ny))
  result.append(cnt)
  


for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      bfs(i, j)
      
result.sort()
print(len(result))
for k in result:
  print(k)
