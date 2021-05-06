#BOJ 15683 - 감시 => DFS
import sys
import copy

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[1, 2], [0, 2], [1, 3], [0, 3]],
    [[1, 2, 3], [0, 1, 2], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
]

n, m = map(int, input().split())
graph = []
combi = []
num = 0
for i in range(n):
     data = list(map(int, input().split()))
     graph.append(data)
     for j in range(m):
         if data[j] in [1, 2, 3, 4, 5]:
             num += 1
             combi.append([data[j], i, j])




def fill(x, y, arr, mm):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if arr[nx][ny] == 6:
                break

            if arr[nx][ny] == 0:
                arr[nx][ny] = 7

def dfs(arr, cnt):
    global min_value
    temp = copy.deepcopy(arr)
    if cnt == num:
        cc = 0
        for i in range(n):
            cc += temp[i].count(0)
        min_value = min(min_value, cc)
        return
    cctv, x, y = combi[cnt]
    for i in mode[cctv]:
        fill(x, y, temp, i)
        dfs(temp, cnt+1)
        temp = copy.deepcopy(arr)




min_value = int(1e9)
dfs(graph, 0)
print(min_value)

