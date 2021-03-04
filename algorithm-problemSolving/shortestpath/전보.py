# 다익스트라 알고리즘 - 우선 순위 큐 이용
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, k = map(int, input().split())
    graph[a].append((b, k))

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

dijkstra(c)
count = 0
max_distance = 0
for d in distance:
    if distance[k] != INF:
        count += 1
        max_distance = max(max_distance, d)

print((count -1), max_distance)



