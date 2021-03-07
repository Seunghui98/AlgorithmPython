# BOJ 특정한 최단 경로 1504번
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    return distance

d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

dd = min(d1[v1] + d2[v2] + d3[n], d1[v2] + d3[v1] + d2[n])
print(dd if dd < INF else -1)


