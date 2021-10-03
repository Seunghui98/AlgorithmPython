# 11724 - BOJ 연결요소의 개수
# BFS
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]


for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque()
    if visited[x] == 0:
        q.append(x)
        visited[x] = x
        while q:
            now = q.popleft()
            for i in graph[now]:
                if visited[i] != 0:
                    continue
                else:
                    visited[i] = x
                    q.append(i)

for i in range(1, n+1):
    bfs(i)

answer_list = visited[1:]
my_set = set(answer_list)
answer_list = list(my_set)
print(len(answer_list))
