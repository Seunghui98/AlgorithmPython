# 이코테 커리큘럼 - 위상 정렬 알고리즘 이용
from collections import deque
import copy

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
cost = [0] * (n+1)
for k in range(n):
  data = list(map(int, input().split()))
  cost[k+1] = data[0]
  for i in range(1, len(data)):
    if data[i] == -1:
      break
    else:
      graph[data[i]].append(k+1)
      indegree[k+1] += 1



def topology_sort():
  result = copy.deepcopy(cost)
  q = deque()

  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    for i in graph[now]:
      indegree[i] -= 1
      result[i] = max(result[i], result[now] + cost[i])

      if indegree[i] == 0:
        q.append(i)

  for o in range(1, n+1):
    print(result[o])



topology_sort()





