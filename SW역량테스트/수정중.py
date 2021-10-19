import copy
n, m, k = map(int, input().split())
s_dir = []

board = []

shark_xy = [[] for _ in range(m)]
out = []
for i in range(n):
    data = list(map(int, input().split()))
    arr = []
    for j in range(n):
        if data[j] != 0:
            arr.append([data[j]-1, k])
            shark_xy[data[j]-1] = [i, j]
        else:
            arr.append([0, 0])
    board.append(arr)
shark_dir = list(map(int, input().split()))
for i in range(m):
    a, b = shark_xy[i]

for _ in range(m):
    dir = []
    for i in range(4):
        data = list(map(int, input().split()))
        dir.append(data)
    s_dir.append(dir)


def move_shark():
    b = [[] * n for _ in range(n)]
    for i in range(m):
        if i in out:
            continue
        x, y = shark_xy[i]
        d = shark_dir[i]-1
        for j in range(2):
            what = False
            for q in range(4):
                nx = x + s_dir[i][d][q]
                ny = y + s_dir[i][d][q]
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if j == 0:
                    if board[nx][ny][0] == 0:
                        x, y = nx, ny
                        d = s_dir[i][d][q]
                        what = True
                        break
                else:
                    if board[nx][ny][0] == i:
                        x, y = nx, ny
                        d = s_dir[i][d][q]
                        what = True
                        break
            if what:
                break
        b[x][y].append(i)
        shark_xy[i] = [x, y]
        board[x][y][0] = i
        board[x][y][1] = k

    for i in range(n):
        for j in range(n):
            if len(b[i][j]) > 1:
                b[i][j].sort()


def count_down():
    for i in range(n):
        for j in range(n):
            if board[i][j][0] == 0:
                continue
            else:
                if board[i][j][1] == 1:
                    board[i][j][0], board[i][j][1] = 0, 0
                else:
                    board[i][j][1] -= 1

count = 0

while True:
    if count > 1000:
        count = -1
        break
    count_down()
    move_shark()
    count += 1
    print(len(out))
    if len(out) == m-1:
        print(len(out))
        break

print(count)
