dice = list(map(int, input().split()))

horse = [0, 0, 0, 0]

connet = [0 for _ in range(33)]
# 외곽(1 ~ 20)
for i in range(21):
    connet[i] = i+1
# 도착
connet[21] = 21
# 10번 다음 (22 ~ 24)
connet[22], connet[23], connet[24] = 23, 24, 30
# 20번 다음 (25 ~ 26)
connet[25], connet[26] = 26, 30
# 30번 다음 (27 ~ 29)
connet[27], connet[28], connet[29] = 28, 29, 30
# 가운데(25) ~ 40전
connet[30], connet[31], connet[32] = 31, 32, 20

# 점수
board = [0 for _ in range(33)]
for i in range(1, 21):
    board[i] = i * 2
board[21] = 0
board[22], board[23], board[24] = 13, 16, 19
board[25], board[26] = 22, 24
board[27], board[28], board[29] = 28, 27, 26
board[30], board[31], board[32] = 25, 30, 35
dul = [0 for _ in range(33)]
def dfs(depth, score):
    global score_max
    if depth == 10:
        score_max = max(score_max, score)
        return

    for i in range(4):
        # 말 현재 위치에서 주사위 만큼 이동
        x, now_x, num = horse[i], horse[i], dice[depth]
        if x in [5, 10, 15]:
            if x == 5:
                x = 22
            elif x == 10:
                x = 25
            else:
                x = 27
            num -= 1
        if x + num <= 21:
            x += num
        else:
            for _ in range(num):
                x = connet[x]
        if dul[x] and x != 21:
            continue
        dul[now_x], dul[x], horse[i] = 0, 1, x
        dfs(depth+1, score+board[x])
        dul[now_x], dul[x], horse[i] = 1, 0, now_x
score_max = 0
dfs(0, 0)
print(score_max)
