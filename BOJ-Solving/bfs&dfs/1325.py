# 효율적인 해킹 - BOJ 1325
# BFS + 방문 최대값
import sys
from collections import deque

input=sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
def bfs(start):
    q = deque()
    count = 0
    q.append(start)
    visited = [0] * (n+1)
    visited[start] = 1
    while q:
        now = q.popleft()
        count += 1
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
    return count

max_value = 0
result = []
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, n+1):
    if graph[i]:
        tmp = bfs(i)
        if max_value <= tmp:
            if max_value < tmp:
                result = []

            max_value = tmp
            result.append(i)

for r in result:
    print(r, end=' ')
