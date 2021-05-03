#BOJ 14891 톱니바퀴 - DFS, 
import sys, collections


graph = []

for _ in range(4):
    graph.append(collections.deque(list(input())))

#왼쪽 톱니바퀴 확
def left(now, dir):
    if now < 0:
        return
    if graph[now][2] != graph[now+1][6]:
        left(now-1, -dir)
        graph[now].rotate(dir)

#오른쪽 톱니바퀴 확인
def right(now, dir):
    if now > 3:
        return
    if graph[now][6] != graph[now-1][2]:
        right(now+1, -dir)
        graph[now].rotate(dir)

for _ in range(int(input())):
    now, dir = map(int, input().split())
    now -= 1
    left(now-1, -dir)
    right(now+1, -dir)
    graph[now].rotate(dir)

result  = 0


for i in range(4):
    if graph[i][0] == '1':
        result += (2**i)

print(result)
