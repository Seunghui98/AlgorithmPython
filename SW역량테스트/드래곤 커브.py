# 드래곤 커브 - BOJ 15685
# Stack + 구현
import copy
n = int(input())
visited = [[False] * (101) for _ in range(101)]

# 동 - 북 - 서 - 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dragon(x, y, dir, g):
    stack = []
    visited[x][y] = True
    nx, ny = x + dx[dir], y + dy[dir]
    visited[nx][ny] = True
    stack.append(dir)
    for i in range(1, g+1):
        stack_copy = copy.deepcopy(stack)
        while stack_copy:
            d = stack_copy.pop()
            d = (d + 1) % 4
            nx += dx[d]
            ny += dy[d]
            visited[nx][ny] = True
            stack.append(d)

for _ in range(n):
    x, y, d, g = map(int, input().split())
    dragon(y, x, d, g)


count = 0


for i in range(0, 100):
    for j in range(0, 100):
        if visited[i][j] and visited[i+1][j] and visited[i][j+1] and visited[i+1][j+1]:
            count += 1

print(count)
