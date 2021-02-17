import sys
sys.setrecursionlimit(50000) #재귀제한높이설정(기본값이상으로 설정 안해주면 런타임 에러) 기본값 : 1000

t = int(input())
total = []
def dfs(x, y, n, m):
  if x<= -1 or x >= n or y <= -1 or y >=m:
    return False
  
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1, y, n, m)
    dfs(x, y-1, n, m)
    dfs(x+1, y, n, m)
    dfs(x, y+1, n, m)
    return True
  return False

for _ in range(t):
  m, n, k = map(int, input().split())
  graph = [[0]*(m) for _ in range(n)]

  for _ in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1

  result = 0

  for i in range(n):
    for j in range(m):
      if dfs(i, j, n, m) == True:
        result += 1
  total.append(result)
  
for k in total:
  print(k)
