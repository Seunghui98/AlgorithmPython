#dfs와 bfs동시 구현
from collections import deque

def dfs(v):
  print(v, end=' ')
  visited[v] = True
  for e in graph[v]:
    if not(visited[e]):
      dfs(e)

def bfs(v):
  queue = deque([v])
  visited[v] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for j in graph[v]:
      if not(visited[j]):
        queue.append(j)
        visited[j] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in graph:
  i.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
