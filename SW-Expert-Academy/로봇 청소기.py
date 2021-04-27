# BOJ 14503 - 로봇 청소기 (시뮬레이션 - 까다롭게 구현)
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
a, b, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(n):
    graph.append(list(map(int, input().split())))

def cheack_boundary(x, y):
    if 0 < x <= n and 0 < y <= m:
        return True
    return False

def change_dir(i):
    if i == 0:
        return 3
    else:
        return i-1

def back(i):
    return (i+2) % 4

def solve(x, y, di):
    count = 1
    q = deque()
    q.append((x, y, di))
    while q:
        x, y, di = q.popleft()
        temp_di = di
        graph[x][y] = 2
        for i in range(4):
            temp_di = change_dir(temp_di)
            nx = x + dx[temp_di]
            ny = y + dy[temp_di]

            if cheack_boundary(nx, ny) and graph[nx][ny] == 0:
                count += 1
                graph[nx][ny] = 2
                q.append((nx, ny, temp_di))
                break

            if i == 3:
                nx = x + dx[back(temp_di)]
                ny = y + dy[back(temp_di)]
                q.append((nx, ny, temp_di))
                if graph[nx][ny] == 0:
                    count += 1
                    graph[nx][ny] = 2
                if graph[nx][ny] == 1:
                    return count


print(solve(a, b, d))
