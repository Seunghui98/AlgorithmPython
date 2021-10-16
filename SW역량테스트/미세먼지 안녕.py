# 미세먼지 안녕 - BOJ 17144
# 구현r, c, t = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(r)]
m_x = []
m_x_count = 0

for i in range(r):
    if graph[i][0] == -1:
        m_x_count += 1
        m_x.append(i)
    if m_x_count == 2:
        break



def move_dust():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    g = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            x, y = i, j
            count = 0
            if graph[x][y] == 0:
                continue
            if graph[x][y] == -1:
                g[x][y] = -1
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                    count += 1
                    g[nx][ny] += int(graph[x][y] // 5)
            g[x][y] += (graph[x][y] - int(graph[x][y] // 5) * count)

    for i in range(r):
        for j in range(c):
            graph[i][j] = g[i][j]

def move_air_up():
    # 동 - 북- 서 - 남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    now, dir = 0, 0
    x, y = m_x[0], 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x == m_x[0] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue
        graph[x][y], now = now, graph[x][y]
        x, y = nx, ny

def move_air_down():
    # 동 - 남 - 서 - 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    now, dir = 0, 0
    x, y = m_x[1], 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x == m_x[1] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue

        graph[x][y], now = now, graph[x][y]
        x, y = nx, ny


for i in range(t):
    move_dust()
    move_air_up()
    move_air_down()


answer = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            answer += graph[i][j]

print(answer)
