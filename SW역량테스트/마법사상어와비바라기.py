# 마법사 상어와 비바라기 - BOJ 21610
# 구현 + queue
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

q = deque()
q.append([n-2, 0])
q.append([n-2, 1])
q.append([n-1, 0])
q.append([n-1, 1])

for _ in range(m):
    cloud = [[0]*n for _ in range(n)]
    d, s = map(int, input().split())
    while q:
        x, y = q.popleft()
        nx = (x + dx[d-1]*s) % n
        ny = (y + dy[d-1]*s) % n
        cloud[nx][ny] = 1

    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                board[i][j] += 1

    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                x, y = i, j
                cnt = 0
                for k in [1, 3, 5, 7]:
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] > 0:
                            cnt += 1
                board[x][y] += cnt

    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and cloud[i][j] == 0:
                board[i][j] -= 2
                q.append([i, j])


s = 0
for i in range(n):
    s += sum(board[i])
print(s)
