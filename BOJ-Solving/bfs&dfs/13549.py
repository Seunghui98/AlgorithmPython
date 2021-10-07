# 숨바꼭질3 - BOJ 13549
# BFS + DP

import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
dx =[1, -1]

visited = [100000 for _ in range(100001)]
time_max = 100000
def bfs(start, end):
    global time_max
    q = deque()
    q.append((start, 0))
    visited[start] = 0
    while q:
        now, time = q.popleft()
        if time >= time_max:
            continue
        for i in range(3):
            if i == 2:
                nx = 2 * now
                new_time = time
            else:
                nx = now + dx[i]
                new_time = time + 1

            if 0 <= nx <= 100000:
                if visited[nx] > new_time:
                    visited[nx] = new_time
                    q.append((nx, new_time))
                    if nx == k:
                        time_max = min(time_max, time)


bfs(n, k)
print(visited[k])
