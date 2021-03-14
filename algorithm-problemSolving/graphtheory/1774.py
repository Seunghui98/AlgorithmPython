# BOJ 우주신과의 교감 1774번 - 크루스칼 알고리즘
import sys

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

input = sys.stdin.readline


n, m = map(int, input().split())

parent = [0] * (n+1)
edges = []
result = 0
x = []
y = []

for i in range(1, n+1):
  parent[i] = i


for _ in range(n):
  a, b = map(int, input().split())
  x.append(a)
  y.append(b)

for _ in range(m):
    n1, n2 = map(int, input().split())
    union_parent(parent, n1, n2)

for i in range(0, n-1):
  for j in range(i+1, n):
    dist = (((x[i] - x[j]) ** 2) + ((y[i] - y[j])**2))**0.5
    edges.append((dist, i+1, j+1))


edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print('%0.2f' % result)
