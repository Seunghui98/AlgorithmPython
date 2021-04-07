# BOJ - 14502번 - BFS로 품
import sys
import copy
from collections import deque
from itertools import combinations


input = sys.stdin.readline

n, m = map(int, input().split())
room = []
virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

array = []
answer = 0

def bfs(graph, virus):
    cc = 0
    global answer
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    for k in range(len(virus)):
        x, y = virus[k][0], virus[k][1]
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if graph[nx][ny] == 1:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cc += 1

    answer = max(answer, cc)




for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j] == 0:
            room.append((i, j))
        elif data[j] == 2:
            virus.append((i, j))
    array.append(data)


room_wall = list(combinations(room, 3))

for i in range(len(room_wall)):
    graph = copy.deepcopy(array)
    for k in range(3):
        graph[room_wall[i][k][0]][room_wall[i][k][1]] = 1
    bfs(graph, virus)

print(answer)
