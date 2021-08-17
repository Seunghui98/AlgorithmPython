# BOJ 트리의 지름1 - 1167번
# 트리 - BFS 2번
# (https://blog.myungwoo.kr/112) - 증명
import sys
from collections import deque

input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    data = list(map(int, input().split()))
    for d in range(1, len(data)-2, 2):
        graph[data[0]].append((data[d], data[d+1]))

def bfs(start):
    visited = [-1] * (v+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    max_len = [0, 0]

    while q:
        x = q.popleft()
        for n, value in graph[x]:
            if visited[n] == -1:
                visited[n] = visited[x] + value
                q.append(n)
                if max_len[0] < visited[n]:
                    max_len = visited[n], n
    return max_len

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)

