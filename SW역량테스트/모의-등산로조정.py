# SWEA - 등산로 조정
# DFS
T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(depth, x, y, val, flag):
    global max_leng
    if max_leng < depth:
        max_leng = depth

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
            if board[nx][ny] < val:
                visited[nx][ny] = True
                dfs(depth+1, nx, ny, board[nx][ny], flag)
            else:
                if flag:
                    for c in range(1, k+1):
                        if (board[nx][ny]-val+1) <= c and (board[nx][ny]-c) >= 0:
                            visited[nx][ny] = True
                            dfs(depth+1, nx, ny, board[nx][ny]-c, False)
            visited[nx][ny] = False
    return

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_leng = 0
    max_value = 0
    for i in range(n):
        max_value = max(max_value, max(board[i]))
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == max_value:
                visited[i][j] = True
                dfs(1, i, j, max_value, True)
                visited[i][j] = False

    print(f'#{test_case} {max_leng}')
