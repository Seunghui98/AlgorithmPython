#BOJ 18428 감시피하기 
from itertools import combinations
import sys
import copy


input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
tt = []
xx = []
n = int(input())
visited = [[0] * n for _ in range(n)]
def bfs(data, tt):
    for x, y in tt:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    break
                if data[nx][ny] == "O":
                    break
                if data[nx][ny] == "S":
                    return False
                nx += dx[i]
                ny += dy[i]
    return True



for i in range(n):
    data = list(input().split())
    graph.append(data)
    for j in range(n):
        if data[j] == 'T':
            tt.append([i, j])
        if data[j] == 'X':
            xx.append([i, j])

cb = list(combinations(xx, 3))

result = False

for i in range(len(cb)):
    what = False
    data = copy.deepcopy(graph)
    for k in range(3):
        data[cb[i][k][0]][cb[i][k][1]] = "O"

    if bfs(data, tt) == True:
        result = True


if result:
    print("YES")
else:
    print("NO")
