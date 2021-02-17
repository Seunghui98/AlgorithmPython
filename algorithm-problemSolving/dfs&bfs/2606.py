# BOJ 바이러스 문제
from collections import deque

def bfs(v):
  result = 0
  queue = deque([v])
  visited[v] = True
  while queue:
    v = queue.popleft()
    for j in graph[v]:
      if not(visited[j]):
        queue.append(j)
        result += 1
        visited[j] = True
  return result



n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in graph:
  i.sort()

visited = [False] * (n+1)
visited = [False] * (n+1)
print(bfs(1))
