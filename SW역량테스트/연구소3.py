# 연구소 3 - BOJ 17142
# BFS + DFS
from collections import deque
import copy
n, m = map(int, input().split())
graph = []
virus = []
min_time = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        if data[j] == 2:
            graph[i][j] = -1
            virus.append((i, j))

def check(g):
    for i in range(n):
        for j in range(n):
            if g[i][j] == 0:
                return False
    return True


def combination(lst, num):
    result = []
    if num > len(lst):
        return result
    if num == 1:
        for l in lst:
            result.append([l])
    elif num > 1:
        for i in range(len(lst)-num+1):
            for temp in combination(lst[i+1:], num-1):
                result.append(temp+[lst[i]])
    return result

def bfs(g, combi):
    global min_time
    visited = [[False]*n for _ in range(n)]
    q = deque()
    if check(g):
        min_time = min(min_time, 0)
        return

    for c in combi:
        a, b = c
        visited[a][b] = True
        g[a][b] = -2
        q.append((a, b, 0))
    end_time = 0
    while q:
        x, y, time = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if g[nx][ny] == 1:
                    continue
                else:
                    if g[nx][ny] == 0:
                        end_time = max(end_time, time + 1)
                    g[nx][ny] = -2
                    visited[nx][ny] = True
                    q.append((nx, ny, time+1))

    if check(g):
        min_time = min(min_time, end_time)


g = copy.deepcopy(graph)
for combi in combination(virus, m):
    g = copy.deepcopy(g)
    bfs(g, combi)
    g = graph

if min_time == int(1e9):
    print(-1)
else:
    print(min_time)
