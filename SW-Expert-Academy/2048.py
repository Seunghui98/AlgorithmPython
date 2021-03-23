# 풀이 참조 (https://dailyheumsi.tistory.com/64)
# BOJ 12100
import sys
from collections import deque
from copy import deepcopy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def move(board, di):
    # can_merged[i][j] 는 (i, j) 번째 블록이 합쳐질 수 있는지를 bool 타입으로 담음
    can_merged = [[True] * n for _ in range(n)]

    # 움직이는 방향에 따라, 반복문의 진행방향이 다르다
    # 위 또는 왼쪽으로 이동하는 경우
    if di in [0, 3]:
        start_idx, end_idx, step = 0, n, 1
    # 아래 또는 오른쪽으로 이동하는 경우
    else:
        start_idx, end_idx, step = n-1, -1, -1

    # 현재 판의 모든 좌표를 탐색하며, 움직임이 필요한 값들은 움직인다
    for i in range(start_idx, end_idx, step):
        for j in range(start_idx, end_idx, step):
            if board[i][j] == 0:
                continue
            x, y = i, j
            value = board[x][y]
            board[x][y] = 0
            nx, ny = x + dx[di], y + dy[di]
            while True:
                # 범위 체크
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break

                # 다음 이동 좌표(nx, ny)가 비어있는 경우, 현재 좌표(x, y)로 이동.
                if board[nx][ny] == 0:
                    x, y = nx, ny
                    nx, ny = x + dx[di], y+ dy[di]

                # 다음 이동 좌표에 현재 이동하는 숫자와 같은 값인 경우, 해당 좌표를 합쳐진 상태로 바꿈
                elif board[nx][ny] == value and can_merged[nx][ny]:
                    x, y = nx, ny
                    can_merged[x][y] = False
                    break

                # 다음 이동 좌표가 비어있지도 않고, 같은 값도 아닌 경우, 움직임 종료
                else:
                    break
            board[x][y] = board[x][y] + value

    return board

def bfs(board):
    q = deque([board])
    max_value = -1
    step = 0

    while q:
        size = len(q)
        for _ in range(size):
            board = q.popleft()
            
            for di in range(4):
                # 새로운 판을 만들어야 하므로, 반드시 deepcopy
                next_board = move(deepcopy(board), di)
                q.append(next_board)

                # 새로 만든 판에 가장 큰 값을 조사한다.
                for i in range(n):
                    for j in range(n):
                        if next_board[i][j] > max_value:
                            max_value = next_board[i][j]
        step += 1

        if step == 5:
            return max_value

print(bfs(board))
