def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

edges = []

n = int(input())
node = [[]]
parent = [0] * (n+1)
for _ in range(n):
  x, y, z = map(int, input().split())
  node.append([x, y, z])

for i in range(1, n+1):
  for j in range(i+1, n+1):
    cost = min(abs(node[i][0]-node[j][0]), abs(node[i][1]-node[j][1]), abs(node[i][2]-node[j][2]))
    edges.append((cost, i, j))


for i in range(1, n+1):
  parent[i] = i

result = 0
edges.sort()

for edge in edges:
  cc, a, b = edge

  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cc

print(result)
