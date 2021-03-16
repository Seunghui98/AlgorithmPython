# BOJ 우수 마을 1949번 - DFS(Stack) + DP

import sys

input = sys.stdin.readline
sys.setrecursionlimit(20000)

n = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
dp = [[0] * 2 for _ in range(n+1)]

def dfs(start):
  visited[start] = True
  dp[start][0] = people[start]
  for i in graph[start]:
    if not visited[i]:
      dfs(i)
      dp[start][0] += dp[i][1]
      dp[start][1] += max(dp[i][0], dp[i][1])

for _ in range(n-1):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

dfs(1)
print(max(dp[1][0], dp[1][1]))

