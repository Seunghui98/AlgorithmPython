# BOJ - 파티 (9019번)
# Prim
import sys
import heapq


input = sys.stdin.readline

n, m, x = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))


def dijkstra(start):
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq, (cost, i[0]))
    return distance



max_value = 0
result = []
dis2 = dijkstra(x)
for i in range(1, n+1):
    if i == x:
        continue
    dis1 = dijkstra(i)
    result.append(dis1[x] + dis2[i])


print(max(result))

