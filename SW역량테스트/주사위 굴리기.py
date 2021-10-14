# 주사위 굴리기 - BOJ 14499
# 구현
import copy
n, m, x, y, k = map(int, input().split())
board = []
# 윗 - 뒤 - 오 - 왼 - 앞 - 바닥
dice = [0, 0, 0, 0, 0, 0]

# 동 - 서 - 북 - 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move_east():
    # 바닥 - 왼 - 윗 - 오 - 바닥
    dice_copy = copy.deepcopy(dice)
    dice[3] = dice_copy[-1]
    dice[0] = dice_copy[3]
    dice[2] = dice_copy[0]
    dice[-1] = dice_copy[2]

def move_west():
    # 바닥 - 오 - 윗 - 왼 - 바닥
    dice_copy = copy.deepcopy(dice)
    dice[2] = dice_copy[-1]
    dice[0] = dice_copy[2]
    dice[3] = dice_copy[0]
    dice[-1] = dice_copy[3]

def move_north():
    # 바닥 - 앞 - 윗 - 뒤 - 바닥
    dice_copy = copy.deepcopy(dice)
    dice[4] = dice_copy[-1]
    dice[0] = dice_copy[4]
    dice[1] = dice_copy[0]
    dice[-1] = dice_copy[1]

def move_south():
    # 바닥 - 뒤 - 윗 - 앞 - 바닥
    dice_copy = copy.deepcopy(dice)
    dice[1] = dice_copy[-1]
    dice[0] = dice_copy[1]
    dice[4] = dice_copy[0]
    dice[-1] = dice_copy[4]

for _ in range(n):
    b = list(map(int, input().split()))
    board.append(b)

moving = list(map(int, input().split()))

nx, ny = x, y
for mv in moving:
    nx += dx[mv-1]
    ny += dy[mv-1]
    if 0 > nx or nx > n-1 or ny < 0 or ny > m-1:
        nx -= dx[mv - 1]
        ny -= dy[mv - 1]
        continue
    if mv == 1:
        move_east()
    elif mv == 2:
        move_west()
    elif mv == 3:
        move_north()
    else:
        move_south()
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
        print(dice[0])
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0
        print(dice[0])
