# BOJ SW 삼성 역테 3190 뱀 -> 구현(시뮬레이션)

import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dir_change(i, dir):
    if dir == 'L':
        if i == 0:
            return 3
        else:
            return i-1
    else:
        if i == 3:
            return 0
        else:
            return i+1

n = int(input())
k = int(input())
long = 1
count = 0
graph = [[False] * (n+1) for _ in range(n+1)]

change = []
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

l = int(input())
for _ in range(l):
    second, dir = input().split()
    change.append([int(second), dir])

snake = [(1, 1)]
d = 0
while True:
    x, y = snake[0]
    for i in range(l):
        if count == change[i][0]:
            d = dir_change(d, change[i][1])
    x += dx[d]
    y += dy[d]
    count += 1
    if x < 1 or x > n or y < 1 or y > n:
        break
    if long > 1:
        if (x, y) in snake[1:long]:
            break
    if graph[x][y]:
        graph[x][y] = False
        long += 1
        snake.insert(0, (x, y))
        continue


    del snake[-1]
    snake.insert(0, (x, y))

print(count)




