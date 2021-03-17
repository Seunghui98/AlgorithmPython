# 구슬탈출2 - BOJ 13460번 - BFS 이용
# 풀이해설 참조(https://wlstyql.tistory.com/72)
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
# 빨간 구슬과 파란 구슬의 방문 여부 체크
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0 # 초기화
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    # 탐색 횟수 1부터 시작
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    count = 0 # 이동 칸 수
    # 다음이 벽이거나 현재가 구멍일 때까지
    while board[x+dx][y+dy] != "#" and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    pos_init() # 시작 조건
    while queue:
        rx, ry, bx, by, depth = queue.pop()
        if depth > 10: # 실패 조건
            break
        for i in range(4): # 4방향으로 탐색
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] != "O": # 실패 조건이 아니면
                if board[nrx][nry] == 'O': # 성공 조건
                    print(depth)
                    return
                if nrx == nbx and nry == nby: # 겹쳤을 때
                    if rcnt > bcnt: # 이동거리가 많은 것을 한 칸 뒤
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                # 탐색 후, 빙문 여부 체크
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    # 다음 너비 우선 탐색을 위해 큐에 삽입
                    queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1) # 실패

bfs()
