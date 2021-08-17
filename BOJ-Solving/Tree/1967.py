# 트리의 지름2 - BOJ 1967
# BFS 2번
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2, dis = map(int, input().split())
    graph[n1].append((n2, dis))
    graph[n2].append((n1, dis))

def bfs(start):
    visited = [-1] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    max_value = [0, 0]
    while q:
        x = q.popleft()
        for y, dis in graph[x]:
            if visited[y] == -1:
                visited[y] = visited[x] + dis
                q.append(y)
                if max_value[0] < visited[y]:
                    max_value = visited[y], y

    return max_value


dis, node = bfs(1)
dis, node = bfs(node)

print(dis)
