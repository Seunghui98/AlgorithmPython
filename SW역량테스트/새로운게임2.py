# 새로운 게임 - BOJ 17837
# 구현
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chess = [[[] for _ in range(n)] for _ in range(n)]
# 동 - 서 - 북 - 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
horse = []

for i in range(k):
    x, y, d = map(int, input().split())
    horse.append([x-1, y-1, d-1])
    chess[x-1][y-1].append(i)

count = 0


def change_dir(d):
    if d in [0, 2]:
        d += 1
    elif d in [1, 3]:
        d -= 1
    return d

def solve(h_num):
    x, y, d = horse[h_num]
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 > nx or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
        d = change_dir(d)
        horse[h_num][2] = d
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 > nx or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
            return True

    chess_up = []

    for h_up, h_n in enumerate(chess[x][y]):
        if h_n == h_num:
            chess_up.extend(chess[x][y][h_up:])
            chess[x][y] = chess[x][y][:h_up]
            break

    if board[nx][ny] == 1:
        chess_up = chess_up[-1::-1]

    for i in chess_up:
        chess[nx][ny].append(i)
        horse[i][:2] = [nx, ny]
    if len(chess[nx][ny]) >= 4:
        return False
    return True



while True:
    what = False
    if count > 1000:
        print(-1)
        break
    for i in range(k):
        if solve(i) == False:
            what = True
            break
    count += 1
    if what:
        print(count)
        break
