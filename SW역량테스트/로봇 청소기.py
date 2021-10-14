# 로봇 청소기 - BOJ 14503
# 구현
n, m = map(int, input().split())
x, y, dir = map(int, input().split())

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [list(map(int, input().split())) for _ in range(n)]

graph[x][y] = 2
answer = 1

def change_dir(dir):
    if dir == 0:
        return 3
    else:
        return dir-1

def solve(x, y, dir):
    global answer
    while True:
        check = False
        for i in range(4):
            n_dir = change_dir(dir)
            nx, ny = x + dx[n_dir], y + dy[n_dir]
            dir = n_dir
            if graph[nx][ny] == 0:
                x, y = nx, ny
                graph[nx][ny] = 2
                check = True
                answer += 1
                break

        if not check:
            back_nx, back_ny = x - dx[dir], y - dy[dir]
            if graph[back_nx][back_ny] == 1:
                return answer
            else:
                x, y = back_nx, back_ny

print(solve(x, y, dir))
