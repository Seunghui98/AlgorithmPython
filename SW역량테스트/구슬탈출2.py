# 구슬탈출 2 - BOJ 13460
# BFS + 구현
from collections import deque

n, m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
rx, ry, bx, by = 0, 0, 0, 0
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    data = list(input())
    graph.append(data)
    for d in range(len(data)):
        if data[d] == 'R':
            rx, ry = i, d
        elif data[d] == 'B':
            bx, by = i, d

def move(x, y, dx, dy):
    count = 0
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    while q:
        r_x, r_y, b_x, b_y, depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            r_nx, r_ny, r_cnt = move(r_x, r_y, dx[i], dy[i])
            b_nx, b_ny, b_cnt = move(b_x, b_y, dx[i], dy[i])
            if graph[b_nx][b_ny] != 'O':
                if graph[r_nx][r_ny] == 'O':
                    return depth
                if r_nx == b_nx and r_ny == b_ny:
                    if r_cnt > b_cnt:
                        r_nx -= dx[i]
                        r_ny -= dy[i]
                    else:
                        b_nx -= dx[i]
                        b_ny -= dy[i]
                if not visited[r_nx][r_ny][b_nx][b_ny]:
                    visited[r_nx][r_ny][b_nx][b_ny] = True
                    q.append((r_nx, r_ny, b_nx, b_ny, depth+1))
    return -1


print(bfs(rx, ry, bx, by))
