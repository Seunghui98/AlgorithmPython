# 뱀 - BOJ 3190
# Queue + 구현
from collections import deque
n = int(input())
k = int(input())

board = [[0]*n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
change = deque()
for i in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

time = 0
snack = deque()
snack.append((0, 0))
board[0][0] = 2
dir = 0

for i in range(int(input())):
    x, c = map(str, input().split())
    change.append((int(x), c))

def change_dir(c):
    global dir
    if c == 'L':
        if dir == 0:
            dir = 3
        else:
            dir -= 1
    else:
        if dir == 3:
            dir = 0
        else:
            dir += 1

def solve():
    global time, dir
    time_x, c = change.popleft()
    while True:
        if len(snack) == 1:
            tail_x, tail_y = snack[0]
            head_x, head_y = tail_x, tail_y
        else:
            tail_x, tail_y = snack[0]
            head_x, head_y = snack[-1]
        nx = head_x + dx[dir]
        ny = head_y + dy[dir]
        time += 1
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 or board[nx][ny] == 2:
            return
        if board[nx][ny] == 1:
            board[nx][ny] = 2
            snack.append((nx, ny))
        else:
            snack.popleft()
            snack.append((nx, ny))
            board[tail_x][tail_y] = 0
            board[nx][ny] = 2
        if time_x == time:
            change_dir(c)
            if len(change) > 0:
                time_x, c = change.popleft()
    return

solve()
print(time)
