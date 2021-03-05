import sys
import heapq
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = 1
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
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

dijkstra(start)

for p in range(0, n+1):
    if distance[p] == INF:
        distance[p] = 0



mm = max(distance)
print(distance)
print(bisect_left(distance, mm), mm, bisect_right(distance, mm)-bisect_left(distance, mm))
