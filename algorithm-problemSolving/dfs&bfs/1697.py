#BOJ 숨바꼭질 1697번
from collections import deque

n, k = map(int, input().split())

Max = 100001
graph = [0] * Max

queue = deque()
queue.append(n)

def bfs():
  while queue:
      x = queue.popleft()
      if x == k:
        print(graph[x])
        return

      for i in (x-1, x+1, x*2):
        if 0<= i < Max and not graph[i]:
          graph[i] = graph[x] + 1
          queue.append(i)

bfs()
