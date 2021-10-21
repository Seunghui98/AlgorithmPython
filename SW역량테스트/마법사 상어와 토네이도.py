# 마법사 상어와 토네이도 - BOJ 20057
# 구현
n = int(input())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

board = [list(map(int, input().split())) for _ in range(n)]

b_dict = {}

x, y = n // 2, n // 2
s = 1
count = 0
d = 0
go = []
for i in range(1, n):
    go.append(i)
    go.append(i)
go.append(n)
g_idx = 0
b_dict[1] = [x, y, 0]
sand = 0

left = [[0,0,2,0,0],[0,10,7,1,0],[5,-1,0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
right = [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,-1,5],[0,1,7,10,0],[0,0,2,0,0]]
up = [[0,0,5,0,0],[0,10,-1,10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]]
down = [[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,-1,10,0],[0,0,5,0,0]]

def moving(x, y, a, plus):
    global sand
    a_x, a_y = -1, -1
    remain = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            if plus[i+2][j+2] == 0 or plus[i+2][j+2] == -1:
                if plus[i+2][j+2] == -1:
                    a_x, a_y = i+2, j+2
                continue
            temp = int(a*(plus[i+2][j+2]/100))
            remain += temp
            if x+i < 0 or x+i >=n or y+j < 0 or y+j >= n:
                sand += temp
            else:
                board[x+i][y+j] += temp
    if 0 <= x+a_x-2 < n and 0<= y+a_y-2 < n:
        board[x+a_x-2][y+a_y-2] += (a-remain)
    else:
        sand += (a-remain)

for i in range(1, n*n):
    nx = x + dx[d]
    ny = y + dy[d]
    count += 1
    x, y = nx, ny
    if count >= go[g_idx]:
        d = (d+1) % 4
        b_dict[i + 1] = [nx, ny, d]
        g_idx += 1
        count = 0
    else:
        b_dict[i+1] = [nx, ny, d]

for i in range(1, n*n):
    x, y, d = b_dict[i]
    nx, ny, nd = b_dict[i+1]
    if d == 0:
        moving(nx, ny, board[nx][ny],left)
    elif d == 1:
        moving(nx, ny, board[nx][ny], down)
    elif d == 2:
        moving(nx, ny, board[nx][ny], right)
    else:
        moving(nx, ny, board[nx][ny], up)
    board[nx][ny] = 0

print(sand)


