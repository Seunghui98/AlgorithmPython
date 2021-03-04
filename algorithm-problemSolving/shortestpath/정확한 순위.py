# 플로이드 워셜 알고리즘 - 노드의 갯수가 500개 이하일 때 효율적
INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 도달 가능 = A < B 라는 성적 비교 가
  a, b = map(int, input().split())
  graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

count = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, n+1):
        if (graph[i][j] != INF or graph[j][i] != INF) and (graph[i][j] != 0):
            count[i] += 1

result = 0

# print(count) (도달 가능 노드 수 출력)
for p in count:
    if p == (n-1):
        result += 1

print(result)
