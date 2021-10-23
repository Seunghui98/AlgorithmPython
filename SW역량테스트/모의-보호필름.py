# 모의 - 보호필름
# DFS
import copy
T = int(input())

def check(b, d, w, k):
    for j in range(w):
        same = 1
        for i in range(d-1):
            if same == k:
                break
            elif b[i][j] == b[i+1][j]:
                same += 1
            else:
                same = 1
        if same != k:
            return False
    return True

def dfs(depth, idx, board2, k):
    global min_answer
    if depth > min_answer:
        return
    if idx == d:
        if check(board2, d, w, k):
            min_answer = depth
        return
    else:
        dfs(depth, idx+1, board2, k)
        for y in range(w):
            board2[idx][y] = 1
        dfs(depth+1, idx+1, board2, k)
        for y in range(w):
            board2[idx][y] = 0
        dfs(depth+1, idx+1, board2, k)
        for y in range(w):
            board2[idx][y] = board[idx][y]

for test_case in range(1, T+1):
    d, w, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(d)]
    board2 = copy.deepcopy(board)
    min_answer = k
    dfs(0, 0, board2, k)
    print(f'#{test_case} {min_answer}')
