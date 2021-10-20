n = int(input())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

board = [[0]*n for _ in range(n)]

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
mx = [-2, 2, -1, 1, -1, 1, -1, 1]
my = [0, 0, 0, 0, -1, -1, 1, 1]

def moving(x, y, d, a):
    if d == 0:
        if x-2 < 0:

        if x+2 >= n:

        if
    elif d == 1:
    elif d == 2:
    else:

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



