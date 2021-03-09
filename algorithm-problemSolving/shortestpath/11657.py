# BOJ 11657 타임머신 - 벨만포드 알고리즘
import sys, collections

INF = float('inf')
graph = collections.defaultdict(list)

input = sys.stdin.readline

n, m = map(int, input().split())
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append([b, c])

def bellman_ford(start):
  distance = [INF] * (n+1)
  distance[start] = 0
  for _ in range(n-1):
    for u in range(1, n+1):
      for v,c in graph[u]:
        if distance[v] > distance[u] + c:
          distance[v] = distance[u] + c

  for u in range(1, n+1):
    for v, c in graph[u]:
      if distance[v] > distance[u] + c:
        return False
  return distance

dist = bellman_ford(1)

if dist == False:
  print(-1)
else:
  for i in range(2, n+1):
    print(dist[i] if dist[i] < INF else -1)
