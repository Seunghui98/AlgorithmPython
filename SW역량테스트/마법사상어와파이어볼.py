n, m, k = map(int, input().split())

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

board = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    r, c, mm, s, d = map(int, input().split())
    board[r-1][c-1].append([mm, s, d])
def move():
    b = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) == 0:
                continue
            for p in board[i][j]:
                x, y = i, j
                mm, s, d = p
                nx = (x + dx[d]*s) % n
                ny = (y + dy[d]*s) % n
                b[nx][ny].append([mm, s, d])

    for i in range(n):
        for j in range(n):
            if len(b[i][j]) <= 1:
                continue
            mm_sum, s_sum, a_odd, a_even = 0, 0, True, True
            num = len(b[i][j])
            for p in b[i][j]:
                mm, s, d = p
                mm_sum += mm
                s_sum += s
                # 홀수
                if (d%2 == 1):
                    a_even = False
                else:
                    a_odd = False
            b[i][j] = []
            if mm_sum < 5:
                continue
            else:
                if a_odd or a_even:
                    for q in [0, 2, 4, 6]:
                        b[i][j].append([mm_sum//5, s_sum//num, q])
                else:
                    for q in [1, 3, 5, 7]:
                        b[i][j].append([mm_sum//5, s_sum//num, q])
    for i in range(n):
        for j in range(n):
            board[i][j] = b[i][j]


for _ in range(k):
    move()

answer = 0
for i in range(n):
    for j in range(n):
        for b in board[i][j]:
            answer += b[0]

print(answer)
