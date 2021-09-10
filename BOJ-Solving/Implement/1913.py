# 달팽이 - BOJ 1913
# 구현 
import sys

input = sys.stdin.readline


n = int(input())
graph = [[0]*n for _ in range(n)]
graph_dict = {}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x = (n+1) // 2 -1
y = (n+1) // 2 -1

index = 1
turn = 0
depth = 1
cnt = 0
while x > -1 and y > -1:
    graph_dict[index] = [x, y]
    graph[x][y] = index
    x += dx[turn]
    y += dy[turn]
    cnt += 1
    index += 1
    if cnt == depth:
        if turn in [1, 3]:
            depth += 1
        turn = (turn + 1) % 4
        cnt = 0

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()

what = int(input())
w_x, w_y = graph_dict[what]
print((w_x+1), (w_y+1))
