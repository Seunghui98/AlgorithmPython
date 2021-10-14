# 테트로미노 - BOJ 14500
# 
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

block = [
    [(0, 1), (1, 0), (1, 1)], # ㅁ
    [(0, 1), (0, 2), (0, 3)], # ㅡ
    [(1, 0), (2, 0), (3, 0)], # ㅣ
    [(1, 0), (2, 0), (2, 1)], # L
    [(0, 1), (0, 2), (1, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (2, 0), (2, -1)],
    [(0, 1), (0, 2), (1, 2)],
    [(0, 1), (1, 0), (2, 0)],
    [(1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (2, 1)],# Z
    [(0, 1), (1, 0), (1, -1)],
    [(0, 1), (1, 1), (1, 2)],
    [(1, -1), (1, 0), (2, -1)],
    [(0, 1), (0, 2), (1, 1)], # ㅜ
    [(1, 0), (1, -1), (2, 0)],
    [(1, 0), (1, -1), (1, 1)],
    [(1, 0), (1, 1), (2, 0)]
]

def solve(x, y):
    global answer
    for i in range(19):
        count = graph[x][y]
        for j in range(3):
            try:
                nx = x + block[i][j][0]
                ny = y + block[i][j][1]
                count += graph[nx][ny]
            except IndexError:
                continue
        answer = max(answer, count)

for i in range(n):
    for j in range(m):
        solve(i, j)
print(answer)
