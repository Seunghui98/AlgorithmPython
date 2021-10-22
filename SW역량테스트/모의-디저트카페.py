# SWEA - 디저트카페
# DFS + 구현
T = int(input())
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def dfs(num, x, y, d):
    global max_cafe
    global sx, sy
    if d == 3 and x == sx and y == sy:
        max_cafe = max(max_cafe, num)
        return
    elif not (0<=x<n and 0<=y<n):
        return
    elif board[x][y] in visited:
        return
    else:
        visited.append(board[x][y])
        if d in [0, 1]:
            dfs(num+1, x+dx[d], y+dy[d], d)
            dfs(num+1, x+dx[d+1], y+dy[d+1], d+1)
        elif d == 2:
            if x + y != sx + sy:
                dfs(num+1, x+dx[2], y+dy[2], 2)
            else:
                dfs(num+1, x+dx[3], y+dy[3], 3)
        else:
            dfs(num+1, x+dx[3], y+dy[3], 3)
        visited.remove(board[x][y])
    return


for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_cafe = -1
    visited = []
    for i in range(n):
        for j in range(n-1):
            sx, sy = i, j
            visited.append(board[i][j])
            dfs(1, i+1, j+1, 0)
            visited.remove(board[i][j])

    print(f'#{test_case} {max_cafe}')
