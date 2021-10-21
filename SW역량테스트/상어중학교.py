# 상어중학교 - BOJ 21609
# 구현 + BFS
import copy
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, b_num):
    q = deque()
    q.append((x, y))
    c = board[x][y]
    visited[x][y] = b_num
    size, r_num = 1, 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < n:
                if board[nx][ny] == c and visited[nx][ny] == 0:
                    size += 1
                    visited[nx][ny] = b_num
                    q.append((nx, ny))
                elif board[nx][ny] == 0 and not b_num in visited[nx][ny]:
                    size += 1
                    r_num += 1
                    visited[nx][ny].append(b_num)
                    q.append((nx, ny))
    return size, r_num




def fall(x, y):
    stop = False
    for i in range(x+1, n):
        nx = i
        if board[nx][y] > -2:
            stop = True
            break
    if stop:
        board[nx-1][y] = board[x][y]
    else:
        board[nx][y] = board[x][y]
    board[x][y] = -2


score = 0
while True:
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                visited[i][j] = []

    b_num, block = 1, []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and visited[i][j] == 0:
                size, mu_cnt = bfs(i, j, b_num)
                if size > 1:
                    block.append([size, mu_cnt, i, j, b_num])
                b_num += 1
    if len(block) == 0:
        break

    block.sort(key=lambda x:(-x[0], -x[1], -x[2], -x[3]))

    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and visited[i][j] == block[0][4]:
                board[i][j] = -2
                count += 1
            elif board[i][j] == 0 and block[0][4] in visited[i][j]:
                board[i][j] = -2
                count += 1

    score += (count * count)

    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] >= 0 and board[i+1][j] == -2:
                fall(i, j)

    board = list(map(list, zip(*board)))[::-1]
    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] >= 0 and board[i+1][j] == -2:
                fall(i, j)


print(score)
