from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        a, b, c = queue.popleft()
        
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]
            if 0 <= x < n and 0 <= y < m and 0 <= z < h and graph[z][x][y] == 0:
                queue.append([x, y, z])
                graph[z][x][y] = graph[c][a][b] + 1
                
m, n, h = map(int, input().split())
graph = [[] for i in range(h)]

queue = deque()
what = False

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append([x, y, z])
bfs()
mm = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                what = True
            mm = max(mm, graph[z][x][y])
if what == True:
    print(-1)
else:
    print(mm - 1)
