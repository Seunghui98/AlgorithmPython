score_max = 0

dice = list(map(int, input().split()))

horse = [0, 0, 0, 0, 0]

board = []
# 외곽(1 ~ 20)
for i in range(1, 21):
    board.append(2*i)
# 도착 (21)
board.append(-1)
# 10번 후 (22 ~24)
for i in range(1, 4):
    board.append(10+i*3)
# 20번 후 (25 ~ 26)
for i in range(1, 3):
    board.append(20+i*2)
# 30번 후 (27 ~ 29)
for i in range(1, 3):
    board.append(29-i)
# 25번 부터 (30 ~ 32)
for i in range(3):
    board.append(25+5*i)

def dfs(depth, score):
    global score_max
    if depth == 10:
        score_max = max(score_max, score)
        return

    for i in range(5):
        if horse.count(horse[i]) > 1:
            continue
        if horse[i] == 10:
            horse[i] = 21
        elif horse[i] == 20:
            horse[i] = 
        elif horse[i] == 30:
        arr = horse[i] + dice[depth]
        if arr == 10:
            
        elif arr == 20:
        elif arr == 30:
        else:
