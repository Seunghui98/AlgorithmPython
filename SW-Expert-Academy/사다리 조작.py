#BOJ 삼성 SW 역테 사다리조작 15684 -> 백트래킹
import sys

input = sys.stdin.readline
min_value = 4

def dfs(count, num):
    global min_value
    if count >= min_value:
        return
    if check():
        min_value = count
        return
    for idx in range(num+1, len(candidates)):
        i, j = candidates[idx]
        if lines[i][j-1] == 0 and lines[i][j+1] == 0:
            lines[i][j] = 1
            dfs(count+1, idx)
            lines[i][j] = 0

def check():
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if lines[j][now] == 1:
                now += 1
            elif lines[j][now-1] == 1:
                now -= 1

        if i != now:
            return False
    return True


n, m, h = map(int, input().split())
lines = [[0 for _ in range(n+1)] for _ in range(h+1)]
candidates = []

for _ in range(m):
    x, y = map(int, input().split())
    lines[x][y] = 1

for i in range(1, h+1):
    for j in range(1, n):
        if lines[i][j-1] == 0 and lines[i][j] == 0 and lines[i][j+1] == 0:
            candidates.append([i, j])

dfs(0, -1)
print(min_value if min_value < 4 else -1)
