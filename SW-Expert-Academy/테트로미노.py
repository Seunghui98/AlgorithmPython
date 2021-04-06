# BOJ 14500번 - 테트로미노
import sys

input = sys.stdin.readline

block = [
    [(0,1), (1,0), (1,1)], # ㅁ
    [(0,1), (0,2), (0,3)], #
    [(1,0), (2,0), (3,0)],
    [(0,1), (0,2), (1,0)], # L
    [(0,1), (0,2), (-1,2)],
    [(1,0), (1,1), (1,2)],
    [(0,1), (0,2), (1,2)],
    [(1,0), (2,0), (2,1)],
    [(0,1), (1,1), (2,1)],
    [(0,1), (1,0), (2,0)],
    [(1,0), (2,0), (2,-1)],
    [(1,0), (1,1), (2,1)], # Z
    [(0,1), (1,0), (-1,1)],
    [(0,1), (1,0), (1,-1)],
    [(0,1), (1,1), (1,2)],
    [(0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,-1)],
    [(1,0), (2,0), (1,-1)],
    [(1,0), (1,1), (2,0)]

]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def tetromino(x, y):
    global answer
    for i in range(19):
        s = a[x][y]
        for j in range(3):
            try:
                nx = x + block[i][j][0]
                ny = y + block[i][j][1]
                s += a[nx][ny]
            except IndexError:
                continue
        answer = max(answer, s)

answer = 0

for i in range(n):
    for j in range(m):
        tetromino(i, j)
        
print(answer)
