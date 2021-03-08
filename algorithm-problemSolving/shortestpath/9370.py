# BOJ 미확인 도착지 9370번
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(n, start):
  distance = [INF] * (n + 1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return distance

for tc in range(int(input())):
  n, m, t = map(int, input().split())
  start, g, h = map(int, input().split())

  graph = [[] for _ in range(n+1)]
  result = []
  for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

  d1 = dijkstra(n, start)
  d2 = dijkstra(n, g)
  d3 = dijkstra(n, h)


  for _ in range(t):
    p = int(input())
    mm = min(d1[g] + d2[h] + d3[p], d1[h] + d3[g] + d2[p])
    if mm == d1[p]:
      result.append(p)
  result.sort()

  for i in result:
    print(i, end=' ')


