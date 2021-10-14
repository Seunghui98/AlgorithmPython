# 2048(Easy) - BOJ 12100
# 구현 + BFS
import copy
from collections import deque
n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def moving(board, d):
    visited = [[False] * n for _ in range(n)]
    if d in [0, 3]:
        start, end, c = 0, n, 1
    else:
        start, end, c = n-1, -1, -1

    for i in range(start, end, c):
        for j in range(start, end, c):
            if board[i][j] == 0:
                continue
            x, y = i, j
            now = board[x][y]
            board[x][y] = 0
            nx = x + dx[d]
            ny = y + dy[d]
            while True:
                if 0 > nx or nx >= n or ny < 0 or ny >= n:
                    break
                elif board[nx][ny] == 0:
                    x, y = nx, ny
                    nx = x + dx[d]
                    ny = y + dy[d]
                elif board[nx][ny] == now and not visited[nx][ny]:
                    x, y = nx, ny
                    visited[x][y] = True
                    break
                else:
                    break
            board[x][y] += now
    return board

def bfs():
    q = deque()
    q.append(board)
    count = 0
    max_value = -1
    while q:
        q_num = len(q)
        for _ in range(q_num):
            b = q.popleft()
            for i in range(4):
                b_copy = copy.deepcopy(b)
                b_copy = moving(b_copy, i)
                q.append(b_copy)
                for i in range(n):
                    for j in range(n):
                        if max_value < b_copy[i][j]:
                            max_value = b_copy[i][j]

        count += 1
        if count >= 5:
            return max_value

print(bfs())
