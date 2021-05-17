#BOJ 15685 드래곤 커브 삼성 SW 역테 - 구현(시뮬레이션), 규칙성 찾기
import sys

#우, 상, 좌, 하
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

input = sys.stdin.readline

n = int(input())
drag = [list(map(int, input().split())) for _ in range(n)]
graph= [[] for _ in range(n)]

for i in range(n):
    x, y, d, g = drag[i]
    graph[i].append(d)
    for _ in range(g):
        reverse = list(reversed(graph[i]))
        for j in reverse:
            if (j+1) == 4:
                graph[i].append(0)
            else:
                graph[i].append(j+1)


arr = [[False] * 101 for _ in range(101)]

for i in range(n):
    x, y, d, g = drag[i]
    arr[y][x] = True
    for j in graph[i]:
        x, y = x + dx[j], y + dy[j]
        if 0 <= x <= 100 and 0 <= y <= 100:
            arr[y][x] = True


result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            result += 1

print(result)


