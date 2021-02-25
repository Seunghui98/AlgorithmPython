# BOJ 이분 그래프 1707번
from collections import deque
import sys

input = sys.stdin.readline
k = int(input())
result = []
def bfs(start):
  bi[start] = 1
  q = deque()
  q.append(start)
  while q:
    a = q.popleft()
    for i in s[a]:
      if bi[i] == 0:
        bi[i] = -bi[a]
        q.append(i)
      else:
        if bi[i] == bi[a]:
          return False
  return True

for i in range(k):
  v, e = map(int, input().split())
  isTrue = True
  s = [[] for _ in range(v+1)]
  bi = [0 for _ in range(v+1)]

  for j in range(e):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)
  
  for m in range(1, v+1):
    if bi[m] == 0:
      if not bfs(m):
        isTrue = False
        break

  result.append("YES" if isTrue else "NO")

for h in result:
  print(h)
