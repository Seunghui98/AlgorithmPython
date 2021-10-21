# 마법사 상어와 파이어스톰 - BOJ 20058
# 구현 + BFS
import copy
from collections import deque

n, q = map(int, input().split())
nn = 2**n
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board= [list(map(int, input().split())) for _ in range(nn)]

def rotate(l):
    b_n = 2**l
    for p1 in range(nn//b_n):
        for p2 in range(nn//b_n):
            b = []
            for i in range(b_n):
                col = []
                for j in range(b_n):
                    col.append(board[b_n*p1+i][b_n*p2+j])
                b.append(col)
            tmp = []
            for item in zip(*b):
                tmp.append(list(reversed(item)))
            for i in range(b_n):
                for j in range(b_n):
                    board[b_n*p1+i][b_n*p2+j] = tmp[i][j]

def dfs(depth, x, y, visited):
    max_m = 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < nn and 0 <= ny < nn:
            if board[nx][ny] > 0 and not visited[nx][ny]:
                max_m += dfs(depth+1, nx, ny, visited)
    return max_m

def bfs(x, y, visited):
    global max_m
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < nn and 0 <= ny < nn and not visited[nx][ny]:
                if board[nx][ny] > 0:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
    max_m = max(max_m, cnt)

l_lst = list(map(int, input().split()))
for l in l_lst:
    if l == n:
        tmp = []
        b = copy.deepcopy(board)
        for item in zip(*b):
            tmp.append(list(reversed(item)))
        board = copy.deepcopy(tmp)
    elif l > 0:
        rotate(l)

    ice = [[0]* nn for _ in range(nn)]

    for i in range(nn):
        for j in range(nn):
            x, y = i, j
            cnt = 0
            if board[i][j] == 0:
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < nn and 0 <= ny < nn:
                    if board[nx][ny] > 0:
                        cnt += 1
            if cnt < 3:
                ice[i][j] = (board[i][j]-1)
            else:
                ice[i][j] = board[i][j]

    board = copy.deepcopy(ice)

s = 0
visited = [[False]*nn for _ in range(nn)]
max_m = 0
for i in range(nn):
    for j in range(nn):
        s += board[i][j]
        if board[i][j] != 0 and not visited[i][j]:
            bfs(i, j, visited)

print(s)
if max_m == 1:
    print(0)
else:
    print(max_m)
